def calculate_safety_index():
    # 사용자로부터 입력 받기
    accident_rate = float(input("사고 발생 확률을 입력하세요 (0과 1 사이의 값): "))
    severity = int(input("사고 발생 시 심각도를 입력하세요 (1부터 5까지의 값): "))

    # 입력 값의 유효성 검사
    if not (0 <= accident_rate <= 1):
        print("입력한 사고 발생 확률이 유효하지 않습니다.")
        return

    if not (1 <= severity <= 5):
        print("입력한 심각도 값이 유효하지 않습니다.")
        return

    # 안전성 지수 계산
    safety_index = (1 - accident_rate) * (5 - severity) * 20

    # 결과 출력
    print(f"안전성 지수는 {safety_index:.2f} 입니다.")

    return safety_index


# 안전성 지수 계산 함수 호출
calculate_safety_index()
