def solution(seat):
    answer = -1

    # 살 수 있는 좌석목록 set
    seat = list((map(tuple,seat)))
    seat_list = list(set(seat))



    return len(seat_list)