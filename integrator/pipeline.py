import importlib
import sys
from typing import List, Tuple, Dict

from reasoner.reasoner import abduce
from parser.parser import parse_story

class Pipeline:
    """推理流水线：B解析 → A推理"""
    
    def __init__(self):
        """初始化，检查A和B是否可用"""
        self._check_modules()
        
    
    def _check_modules(self):
        """检查A和B的接口是否正确"""
        # 检查B
        assert callable(parse_story), "B模块的parse_story不是函数"
        test_facts = parse_story("test")
        assert isinstance(test_facts, list), "B模块返回类型错误"
        
        # 检查A
        assert callable(abduce), "A模块的abduce不是函数"
        test_result = abduce([("test",)])
        assert isinstance(test_result, list), "A模块返回类型错误"
        
    def run(self, story: str, top_k: int = 3) -> Dict:
        """
        运行完整pipeline
        
        Args:
            story: 输入故事文本
            top_k: 返回前几个假设
        
        Returns:
            包含推理结果的字典
        """
        # Step 1: B解析文本 → 符号事实
        try:
            facts = parse_story(story)
        except Exception as e:
            print(f"❌ B解析失败: {e}")
            return self._error_result(story, f"B解析失败: {e}")
        
        # Step 2: A推理 → 假设列表
        try:
            all_hypotheses = abduce(facts)
            hypotheses = all_hypotheses[:top_k]  # 取top_k
        except Exception as e:
            print(f"❌ A推理失败: {e}")
            return self._error_result(story, f"A推理失败: {e}", facts)
        
        # Step 3: 组装结果
        result = self._build_result(story, facts, hypotheses)
        
        return result

    def _build_result(self, story: str, facts: List[Tuple], hypotheses: List[Dict]) -> Dict:
        """组装成功的结果"""
        return {
            "success": True,
            "story": story,
            "facts": facts,
            "hypotheses": hypotheses,
            "best_hypothesis": hypotheses[0]["hypothesis"] if hypotheses else None,
            "best_score": hypotheses[0]["score"] if hypotheses else 0,
            "count": len(hypotheses)
        }
    
    
# 创建全局单例（方便其他地方导入使用）
_pipeline = None

def get_pipeline():
    """获取pipeline单例"""
    global _pipeline
    if _pipeline is None:
        _pipeline = Pipeline()
    return _pipeline