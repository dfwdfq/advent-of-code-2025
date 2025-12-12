#!/usr/bin/env python3
import sys
import signal

class TimeoutException(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutException()

def generate_orientations(shape_points):
    """Generate all distinct rotations and reflections of a shape."""
    # shape_points: list of (r, c) in a 3x3 grid
    
    def rotate90(points):
        return [(c, 2 - r) for (r, c) in points]
    
    def reflect(points):
        return [(r, 2 - c) for (r, c) in points]
    
    orientations = set()
    
    for ref in (False, True):
        transformed = shape_points
        if ref:
            transformed = reflect(transformed)
        for rot in range(4):
            if rot:
                transformed = rotate90(transformed)
            # Normalize: shift so min row and min col are 0
            min_r = min(r for r, _ in transformed)
            min_c = min(c for _, c in transformed)
            normalized = tuple(sorted([(r - min_r, c - min_c) for r, c in transformed]))
            orientations.add(normalized)
    
    return list(orientations)

def parse_input():
    """Parse input file."""
    with open(sys.argv[1], "r") as f:
        content = f.read().strip()
    
    lines = [line.strip() for line in content.split("\n") if line.strip()]
    
    shapes = {}
    regions = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        if ':' in line and 'x' not in line and i + 3 <= len(lines):
            # Shape line (e.g., "0:")
            idx_str, _ = line.split(':', 1)
            idx = int(idx_str.strip())
            
            # Read the next 3 lines for the shape pattern
            pattern_lines = []
            for j in range(1, 4):
                if i + j < len(lines):
                    pattern_lines.append(lines[i + j])
            
            # Convert pattern to points
            pts = []
            for r, row in enumerate(pattern_lines):
                for c, ch in enumerate(row):
                    if ch == '#':
                        pts.append((r, c))
            
            shapes[idx] = pts
            i += 4  # Skip shape index line and 3 pattern lines
        elif ':' in line and 'x' in line:
            # Region line
            left, right = line.split(':', 1)
            w, h = map(int, left.split('x'))
            counts = list(map(int, right.strip().split()))
            regions.append((w, h, counts))
            i += 1
        else:
            i += 1
    
    return shapes, regions

def solve_region(W, H, counts, shapes, shape_orientations, time_limit=2):
    """Solve a single region using backtracking."""
    # Quick area check
    total_cells = 0
    for s in range(6):  # Shapes 0-5
        if s in shapes and len(counts) > s and counts[s] > 0:
            total_cells += counts[s] * len(shapes[s])
    
    if total_cells > W * H:
        return False
    
    # Initialize grid
    grid = [[0] * W for _ in range(H)]
    
    # Build list of shapes to place
    shapes_to_place = []
    for s in range(6):
        if s in shapes and len(counts) > s:
            shapes_to_place.extend([s] * counts[s])
    
    if not shapes_to_place:
        return True
    
    # Sort shapes by number of cells (largest first)
    shapes_to_place.sort(key=lambda s: len(shapes[s]), reverse=True)
    
    def backtrack(idx):
        """Backtracking function."""
        if idx == len(shapes_to_place):
            return True
        
        s = shapes_to_place[idx]
        
        for orientation in shape_orientations[s]:
            # Get bounding box of this orientation
            if not orientation:
                continue
            min_r = min(r for r, _ in orientation)
            max_r = max(r for r, _ in orientation)
            min_c = min(c for _, c in orientation)
            max_c = max(c for _, c in orientation)
            oh = max_r - min_r + 1
            ow = max_c - min_c + 1
            
            # Try all positions
            for r in range(H - oh + 1):
                for c in range(W - ow + 1):
                    # Check if can place
                    valid = True
                    for dr, dc in orientation:
                        nr, nc = r + dr - min_r, c + dc - min_c
                        if grid[nr][nc] == 1:
                            valid = False
                            break
                    
                    if not valid:
                        continue
                    
                    # Place shape
                    for dr, dc in orientation:
                        nr, nc = r + dr - min_r, c + dc - min_c
                        grid[nr][nc] = 1
                    
                    if backtrack(idx + 1):
                        return True
                    
                    # Remove shape
                    for dr, dc in orientation:
                        nr, nc = r + dr - min_r, c + dc - min_c
                        grid[nr][nc] = 0
        
        return False
    
    # Set timeout
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(time_limit)
    
    try:
        result = backtrack(0)
        signal.alarm(0)
        return result
    except TimeoutException:
        signal.alarm(0)
        return False

def main():
    # Parse input
    shapes, regions = parse_input()
    
    # Precompute orientations for each shape
    shape_orientations = {}
    for idx, pts in shapes.items():
        shape_orientations[idx] = generate_orientations(pts)
    
    # Count feasible regions
    feasible = 0
    
    for i, (W, H, counts) in enumerate(regions):
        # Ensure counts list has 6 elements
        if len(counts) < 6:
            counts = counts + [0] * (6 - len(counts))
        
        if solve_region(W, H, counts, shapes, shape_orientations, time_limit=2):
            feasible += 1
        
        # Optional progress indicator
        # if (i + 1) % 100 == 0:
        #     print(f"Processed {i + 1} regions, feasible: {feasible}")
    
    print(feasible)

if __name__ == "__main__":
    main()