from typing import List, Dict, Optional
from integrator.pipeline import get_pipeline


# 获取pipeline实例
_pipeline = get_pipeline()

def reason(story: str, top_k: int = 3, visualize: bool = False) -> Dict:
    """
    核心函数：输入故事，输出推理结果
    
    Args:
        story: 自然语言故事
        top_k: 返回前几个假设
        visualize: 是否生成可视化图片
    
    Returns:
        {
            "success": True/False,
            "story": 原故事,
            "facts": 解析出的事实,
            "hypotheses": 假设列表,
            "best_hypothesis": 最佳假设,
            "best_score": 最佳得分,
            "viz_path": 可视化图片路径(可选)
        }
    """
    # 1. 运行pipeline
    result = _pipeline.run(story, top_k)
        
    return result