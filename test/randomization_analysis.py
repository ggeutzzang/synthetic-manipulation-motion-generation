print("=== Isaac Lab 랜덤화 파라미터 시스템 분석 ===")

# 실제 코드에서 정의된 랜덤화 파라미터
randomizable_params = {
    "randomize_franka_joint_state": {
        "mean": (0.0, 0.5, 0.01),  # (최소, 최대, 단계)
        "std": (0.0, 0.1, 0.01),
    },
    "randomize_cube_positions": {
        "pose_range": {
            "x": (0.3, 0.9, 0.01),  # X축 위치 범위 (미터)
            "y": (-0.3, 0.3, 0.01),  # Y축 위치 범위 (미터)
        },
        "min_separation": (0.0, 0.5, 0.01),  # 큐브 간 최소 거리
    },
}

print("1. 정의된 랜덤화 파라미터:")
for event_name, params in randomizable_params.items():
    print(f"\n   {event_name}:")
    for param_name, values in params.items():
        if isinstance(values, dict):
            print(f"     {param_name}:")
            for sub_param, range_info in values.items():
                min_val, max_val, step = range_info
                print(f"       {sub_param}: {min_val} ~ {max_val} (단계: {step})")
        else:
            min_val, max_val, step = values
            print(f"     {param_name}: {min_val} ~ {max_val} (단계: {step})")

# 시뮬레이션된 event_manager 구조
print(f"\n2. Event Manager 시스템 시뮬레이션:")


class MockEventTerm:
    def __init__(self, func_name):
        self.func = type("MockFunc", (), {"__name__": func_name})()


# 환경에서 발견될 수 있는 이벤트들
mock_event_manager = {
    "_mode_term_cfgs": {
        "reset": [
            MockEventTerm("randomize_franka_joint_state"),
            MockEventTerm("randomize_cube_positions"),
        ]
    },
    "active_terms": {
        "reset": ["randomize_franka_joint_state", "randomize_cube_positions"]
    },
}

print("   발견된 리셋 이벤트들:")
for i, event_term in enumerate(mock_event_manager["_mode_term_cfgs"]["reset"]):
    name = mock_event_manager["active_terms"]["reset"][i]
    print(f"     {i}: {event_term.func.__name__} (이름: {name})")

# 코드 동작 시뮬레이션
print(f"\n3. 코드 동작 시뮬레이션:")
print("   for i in range(len(env.unwrapped.event_manager._mode_term_cfgs['reset'])):")

for i in range(len(mock_event_manager["_mode_term_cfgs"]["reset"])):
    event_term = mock_event_manager["_mode_term_cfgs"]["reset"][i]
    name = mock_event_manager["active_terms"]["reset"][i]

    print(f"\n   반복 {i}:")
    print(f"     event_term: {event_term.func.__name__}")
    print(f"     name: {name}")
    print(f"     params: {randomizable_params.get(name, '매칭되는 파라미터 없음')}")

    if name in randomizable_params:
        print(f"     -> interactive_update_randomizable_params() 호출됨")
        print(f"        이 이벤트에 대한 Jupyter 위젯이 생성됩니다!")

# 랜덤화의 목적과 효과
print(
    f"""
4. 랜덤화의 목적과 효과:

목적:
- 데이터 다양성 확보: 매번 다른 환경 조건에서 시연 생성
- 강건성 향상: 다양한 시나리오에 대응 가능한 정책 학습
- 일반화 능력: 실제 환경의 불확실성을 시뮬레이션에 반영

Franka 관절 랜덤화:
- 로봇 시작 자세를 매번 다르게 설정
- 실제 로봇의 초기 자세 불확실성 모사
- mean=0.1, std=0.05 → 평균 0.1 라디안 오프셋, 표준편차 0.05

큐브 위치 랜덤화:
- x: 0.3~0.9m 범위에서 큐브 배치
- y: -0.3~0.3m 범위에서 큐브 배치  
- min_separation: 큐브들이 너무 가깝게 배치되지 않도록 제한

인터랙티브 조정:
- Jupyter 슬라이더로 실시간 파라미터 변경
- 즉시 환경에 반영되어 효과 확인 가능
- 최적의 랜덤화 수준 실험적으로 결정
"""
)

print("5. 실제 데이터 생성에서의 활용:")
print(
    """
   각 시연(trial) 생성 시:
   1. 환경 리셋
   2. 랜덤화 이벤트 실행
      - Franka 로봇 관절을 랜덤한 각도로 설정
      - 큐브들을 랜덤한 위치에 배치
   3. 모방 학습 알고리즘으로 시연 실행
   4. 성공 시 데이터셋에 저장
   
   → 결과적으로 다양한 조건의 시연 데이터 대량 생성!
"""
)
