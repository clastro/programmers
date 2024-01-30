def solution(citations):
    citations.sort(reverse=True)  # 논문을 내림차순으로 정렬

    h_index = 0
    for i, citation in enumerate(citations, start=1):
        if i <= citation:
            h_index = i
        else:
            break

    return h_index
