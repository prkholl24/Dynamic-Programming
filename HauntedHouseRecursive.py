from pathlib import Path

n = 0
k = 0
rooms = []
solution =[]

def main():
    global n, k, rooms
    load_from_file = True

    if load_from_file:
        load_test_case("test3.txt")

    else:
        nk = list(map(int, input().split()))
        n = nk[0]
        k = nk[1]
        for _ in range(n):
            lr = list(map(int,input().split()))
            rooms.append(lr)
        rooms.pop(0)

    max_scary = max(spooky(0,0,k,False),spooky(0,1,k,False))
    print("The max recursive score is:",max_scary)



def load_test_case(filename: str) -> None:
    global n, k, rooms  
    input_path = Path(__file__).with_name(filename)
    values = [list(map(int, line.split())) for line in input_path.read_text().splitlines()]

    n, k = values[0]
    rooms = values[1:]

    print("successfully loaded test case")



#i: current depth
#m: 0 for left side, 1 for right side, could be bool, but nah
#k: doors closed so far
#e: has opposite side been explored
def spooky(i:int, m:int, k:int,e:bool):
    if k < 0:
        return float("-inf")
    
    if i >= n:
        if k == 0:
            return 0
        return float("-inf")
    
    if k > (n-i):
        return float("-inf")

    if e == False:
        if m == 0:
            return max(spooky(i,m+1,k,True)+rooms[i][m], spooky(i+1,m,k-1,False)+rooms[i][m])
        if m == 1:
            return max(spooky(i,m-1,k,True)+rooms[i][m], spooky(i+1,m,k-1,False)+rooms[i][m])

    else:
        return spooky(i+1, m, k, False)+rooms[i][m] 

    return -1


if __name__ == "__main__":
    main()