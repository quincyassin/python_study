"""
参考版本：学生成绩统计系统 - 主入口
包含：上下文管理器 with + 装饰器 + 生成器管道 + lambda
"""
from utils_ref import (
    read_scores, parse_scores, sort_scores,
    filter_passed, Scorer, timer, log
)


@timer                    # 给整个流程加计时
@log(level="INFO")        # 给整个流程加日志
def main():
    # ---------- 用上下文管理器包裹整个统计流程 ----------
    with Scorer() as scorer:

        # 1. 生成器管道：读文件 → 清洗
        raw = read_scores("scores.csv")
        cleaned = parse_scores(raw)

        # 2. 收集成列表（生成器被消费一次）
        all_scores = list(cleaned)
        scorer.count = len(all_scores)   # 记录有效数据条数

        # 3. 排名（lambda 排序）
        ranked = sort_scores(all_scores)
        print("\n🏆 排名:")
        for s in ranked:
            print(f"  {s['name']}: {s['score']:.1f}")

        # 4. 及格统计（filter + lambda，转 list）
        passed = list(filter_passed(ranked))
        print(f"\n📊 及格人数: {len(passed)}")

        # 5. 加分（列表推导式 + round）
        bonus = [round(s["score"] * 1.1, 1) for s in passed]
        print(f"📈 加分后: {bonus}")


if __name__ == "__main__":
    main()
