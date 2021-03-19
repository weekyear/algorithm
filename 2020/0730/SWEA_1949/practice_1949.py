import sys
import copy

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def get_up_point(self):
        new_x = self.x - 1
        if new_x < 0:
            return None
        return Point(new_x, self.y)
        
    def get_down_point(self):
        new_x = self.x + 1
        if new_x < 0:
            return None
        return Point(new_x, self.y)

    def get_right_point(self):
        new_y = self.y + 1
        if new_y < 0:
            return None
        return Point(self.x, new_y)
    
    def get_left_point(self):
        new_y = self.y - 1
        if new_y < 0:
            return None
        return Point(self.x, new_y)

class GoingState:
    def __init__(self, p, m, c, s, pt_list=list()):
        self.point = p
        self.mountain = copy.deepcopy(m)
        self.chance = c
        self.step = s
        self.pt_list = copy.deepcopy(pt_list)

def go_step(cur_state):
    if cur_state != None:
        left_pos = cur_state.point.get_left_point()
        right_pos = cur_state.point.get_right_point()
        down_pos = cur_state.point.get_down_point()
        up_pos = cur_state.point.get_up_point()
        
        if left_pos == None and down_pos == None and right_pos == None and up_pos == None:
            return cur_state.step
        else:
            step_list = []

            if left_pos != None:
                step_list.append(go_step(calculate_next_state(left_pos, cur_state)))
            if right_pos != None:
                step_list.append(go_step(calculate_next_state(right_pos, cur_state)))
            if down_pos != None:
                step_list.append(go_step(calculate_next_state(down_pos, cur_state)))
            if up_pos != None:
                step_list.append(go_step(calculate_next_state(up_pos, cur_state)))

            while None in step_list:
                step_list.remove(None)

            if len(step_list) > 0:
                return max(step_list)
            else:
                return cur_state.step

def calculate_next_state(pos, cur_state):
    cur_pt = cur_state.point
    if pos.x >= len(cur_state.mountain) or pos.y >= len(cur_state.mountain):
        return None

    if cur_state.mountain[pos.x][pos.y] < cur_state.mountain[cur_pt.x][cur_pt.y]:
        return GoingState(pos, cur_state.mountain, cur_state.chance, cur_state.step + 1, cur_state.pt_list + [pos])
    elif 0 <= cur_state.mountain[pos.x][pos.y] - cur_state.mountain[cur_pt.x][cur_pt.y] < cur_state.chance:
        for pt in cur_state.pt_list:
            if pt.x == pos.x and pt.y == pos.y:
                return None

        if test_case == 4 and cur_state.step == 4:
            d = 0

        cur_state.mountain[pos.x][pos.y] = cur_state.mountain[cur_pt.x][cur_pt.y] - 1
        return GoingState(pos, cur_state.mountain, -10000, cur_state.step + 1, cur_state.pt_list + [pos])

sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    test_cond = list(map(int, input().split()))
    N = test_cond[0]
    K = test_cond[1]

    mountain_origin = []
    for i in range(N):
        mountain_origin.append(list(map(int, input().split())))

    highest_pos_list = []
    max_height = 0

    for h in range(len(mountain_origin)):
        for v in range(len(mountain_origin[h])):
            if mountain_origin[h][v] > max_height:
                max_height = mountain_origin[h][v]
                highest_pos_list.clear()
                highest_pos_list.append([h, v])
            elif mountain_origin[h][v] == max_height:
                highest_pos_list.append([h, v])

    max_step = 0
    for pt in highest_pos_list:
        current_step = go_step(GoingState(Point(pt[0], pt[1]), mountain_origin, K, 1, [Point(pt[0], pt[1])]))
        if current_step > max_step:
            max_step = current_step

    print('#{} {}'.format(test_case, max_step))