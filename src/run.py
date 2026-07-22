from utils.register import registry
import engine
import agents
import hospital
import utils
from utils.options import get_parser


if __name__ == '__main__':
    # 解析命令行参数
    args = get_parser()
    # 根据 --scenario 参数获取对应场景类并实例化（默认 Scenario.Consultation）
    scenario = registry.get_class(args.scenario)(args)
    # 根据 --parallel 参数决定串行或并行执行诊断
    if not args.parallel:
        scenario.run()
    else:
        scenario.parallel_run()
