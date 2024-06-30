import utilities.helper as helper


scenario_test_results = []
start_time = None
end_time = None


def before_all(context):
    global start_time
    helper.delete_json_file("test_result.json")
    start_time = helper.get_current_time()


def before_feature(context, feature):
    global start_time
    start_time = helper.get_current_time()


def before_scenario(context, scenario):
    scenario_info = {
        "name": scenario.name,
        "status": "unknown"
    }
    scenario_test_results.append(scenario_info)


def after_scenario(context, scenario):
    for scenario_info in scenario_test_results:
        if scenario_info["name"] == scenario.name:
            scenario_info["status"] = scenario.status.name
    # add
    context.driver.quit()
    # end
    helper.create_json(scenario_test_results, "test_result.json")


def after_feature(context, feature):
    global start_time, end_time
    end_time = helper.get_current_time()
    time_required = end_time - start_time
    minutes, seconds = divmod(time_required.seconds, 60)
    feature_name = feature.filename
    formatted_time = f"{minutes}분 {seconds}초"
    print(f"{feature_name} 테스트 소요 시간 : {formatted_time}")
