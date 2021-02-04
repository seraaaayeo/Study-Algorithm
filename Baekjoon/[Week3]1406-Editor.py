import sys

def op_L(LStack, RStack):
    if not LStack:
        return
    top = LStack.pop()
    RStack.append(top)
    return LStack, RStack

def op_D(LStack, RStack):
    if not RStack:
        return
    top = RStack.pop()
    LStack.append(top)
    return LStack, RStack

def op_B(LStack, RStack):
    # 커서가 문장의 맨 앞이면 무시됨 -> 커서 왼쪽 스택이 비었을 경우
    if not LStack:
        return
    LStack.pop()
    return LStack

def op_P(LStack, RStack, ch):
    LStack.append(ch)
    return LStack
    
# print operation : 커서 왼쪽에 있는 문자열을 모두 오른쪽에 넣고 출력
def op_print(LStack, RStack):
    while len(LStack) != 0:
        RStack.append(LStack.pop())
    
    print("".join(RStack[::-1]))
        
    
def solution():
    LStack = []
    RStack = []
    
    string = sys.stdin.readline().rstrip()
    for char in string:
        LStack.append(char)
    
    n = int(sys.stdin.readline().rstrip())
    for i in range(n):
        op = sys.stdin.readline().rstrip()
        if op == 'L':
            op_L(LStack, RStack)
        elif op == 'D':
            op_D(LStack, RStack)
        elif op == 'B':
            op_B(LStack, RStack)
        else:
            char = op.split()
            ch = char[-1]
            op_P(LStack, RStack, ch)
            
    op_print(LStack, RStack)
    
if __name__=='__main__':
    solution()