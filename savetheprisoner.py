if __name__ == "__main__":
    t = int(input())
    for i in range(0, t):
        arr = list(map(int, input().split()))
        seat = []
        for i in range(0, arr[0]):
            seat.append(i)
        seat_no = arr[2]-1
        for i in range(0, arr[1]):
            req_seat = seat[seat_no]
            seat_no += 1
            if(seat_no == arr[0]):
                seat_no = 0
        print(req_seat+1)