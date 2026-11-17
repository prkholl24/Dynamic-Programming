from pathlib import Path

n = 0
k = 0
rooms = []
solution =[]

def main():
    global n, k, rooms
    load_from_file = True

    if load_from_file:
        load_test_case("test4.txt")

    else:
        nk = list(map(int, input().split()))
        n = nk[0]
        k = nk[1]
        for _ in range(n):
            lr = list(map(int,input().split()))
            rooms.append(lr)
        rooms.pop(0)

    max_scary = spooky_dynamic(n,k)
    print("The max dynamic score is: ",max_scary)




def load_test_case(filename: str) -> None:
    global n, k, rooms  
    input_path = Path(__file__).with_name(filename)
    values = [list(map(int, line.split())) for line in input_path.read_text().splitlines()]

    n, k = values[0]
    rooms = values[1:]

    print("successfully loaded test case")

    
def spooky_dynamic(n:int, k:int):
    global rooms, solutions

    solution = [[[float("-inf") for _ in range(3)] for _ in range(k+2)] for _ in range(n+1)]
    

    for state in range(3):
        solution[n][0][state] = 0


    for i in range(n-1, -1, -1):
        for doors in range(k+1):
            for m in range(3):

                if doors > 0:
                    if m == 0:
                        solution[i][doors][m] = max(solution[i+1][doors-1][0] + rooms[i][1],
                                                    solution[i+1][doors][2] + rooms[i][1] + rooms[i][0])

                    if m == 1:
                        solution[i][doors][m] = max(solution[i+1][doors-1][1] + rooms[i][0],
                                                    solution[i+1][doors][2] + rooms[i][1] + rooms[i][0])

                    if m == 2: 
                        solution[i][doors][m] = max(solution[i+1][doors-1][0] + rooms[i][1],
                                                    solution[i+1][doors-1][1] + rooms[i][0],
                                                    solution[i+1][doors][2] + rooms[i][1] + rooms[i][0])
                else:
                    if m == 0:
                        solution[i][doors][m] = solution[i+1][doors][2] + rooms[i][1] + rooms[i][0]
                                                    

                    if m == 1:
                        solution[i][doors][m] = solution[i+1][doors][2] + rooms[i][1] + rooms[i][0]

                    if m == 2: 
                        solution[i][doors][m] = solution[i+1][doors][2] + rooms[i][1] + rooms[i][0]


  
    return max(solution[0][k][0], solution[0][k][1], solution[0][k][2])


if __name__ == "__main__":
    main()