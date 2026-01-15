# 3454. Separate Squares II

# You are given a 2D integer array squares. Each squares[i] = [xi, yi, li] represents the coordinates of the bottom-left point and the side length of a square parallel to the x-axis.

# Find the minimum y-coordinate value of a horizontal line such that the total area covered by squares above the line equals the total area covered by squares below the line.

# Answers within 10-5 of the actual answer will be accepted.

# Note: Squares may overlap. Overlapping areas should be counted only once in this version.

class Solution:
    def separateSquares(self, squares):
        # ---------------------------------------------------
        # STEP 1: Convert squares into sweep-line events
        # ---------------------------------------------------
        # Each square [x, y, l] becomes:
        #   + add interval [x, x+l] at y
        #   + remove interval [x, x+l] at y+l
        events = []
        x_coords = set()

        for x, y, l in squares:
            events.append((y, x, x + l, +1))
            events.append((y + l, x, x + l, -1))
            x_coords.add(x)
            x_coords.add(x + l)

        # ---------------------------------------------------
        # STEP 2: Coordinate compression on X-axis
        # ---------------------------------------------------
        xs = sorted(x_coords)
        x_index = {x: i for i, x in enumerate(xs)}
        segment_count = len(xs) - 1

        # ---------------------------------------------------
        # STEP 3: Segment Tree to maintain union width
        # ---------------------------------------------------
        count = [0] * (segment_count * 4)
        covered = [0.0] * (segment_count * 4)

        def update(node, left, right, ql, qr, delta):
            if qr <= left or right <= ql:
                return

            if ql <= left and right <= qr:
                count[node] += delta
            else:
                mid = (left + right) // 2
                update(node * 2, left, mid, ql, qr, delta)
                update(node * 2 + 1, mid, right, ql, qr, delta)

            if count[node] > 0:
                covered[node] = xs[right] - xs[left]
            else:
                if left + 1 == right:
                    covered[node] = 0.0
                else:
                    covered[node] = covered[node * 2] + covered[node * 2 + 1]

        # ---------------------------------------------------
        # STEP 4: Sweep line over Y-axis
        # ---------------------------------------------------
        events.sort()
        prev_y = events[0][0]

        slice_areas = []
        slice_heights = []
        slice_start_y = []

        total_area = 0.0
        i = 0

        while i < len(events):
            curr_y = events[i][0]
            height = curr_y - prev_y

            if height > 0:
                area = covered[1] * height
                slice_areas.append(area)
                slice_heights.append(height)
                slice_start_y.append(prev_y)
                total_area += area

            while i < len(events) and events[i][0] == curr_y:
                _, x1, x2, delta = events[i]
                update(1, 0, segment_count, x_index[x1], x_index[x2], delta)
                i += 1

            prev_y = curr_y

        # ---------------------------------------------------
        # STEP 5: Find Y where area below = total_area / 2
        # ---------------------------------------------------
        half = total_area / 2.0
        accumulated = 0.0

        for i in range(len(slice_areas)):
            if accumulated + slice_areas[i] >= half:
                remaining = half - accumulated
                fraction = remaining / slice_areas[i]
                return slice_start_y[i] + slice_heights[i] * fraction

            accumulated += slice_areas[i]

        return prev_y
