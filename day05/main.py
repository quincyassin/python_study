from utils import (read_scores, 
                   sort_scores, 
                   filter_passed, 
                   parse_scores,
                   Scorer,
                   timer)
@timer
def main():
    with Scorer() as scorer:
        # 清洗数据
        raw = read_scores("scores.csv")
        cleaned = parse_scores(raw)

        # 收集列表 (列表字典)
        all_scores = list(cleaned)
        scorer.count = len(all_scores)   # 记录有效数据条数

        # 排名
        sorted_scores = sort_scores(all_scores)
        print("🏆 排名:")
        for score in sorted_scores:
            print(f"{score['name']}: {score['score']:.2f}")

        # 及格统计
        passed = list(filter_passed(sorted_scores))
        print(f"📊 及格人数: {len(passed)}")

        # 加分
        bonums_scores = [round(float(score["score"]) * 1.1, 2) for score in passed]
        print(f"📈 加分后:{bonums_scores}")

main()