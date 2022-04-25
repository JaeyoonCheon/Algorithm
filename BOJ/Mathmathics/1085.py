"""
1085번 직사각형에서 탈출

1.  두 점 사이의 최소 거리
    root(x^2 + y^2) -> root((x-w)^2 + (y-h)^2)
"""

x, y, w, h = map(int, input().split())

print(min(x, y, (w - x), (h - y)))
