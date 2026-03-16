# D
## D需要的接口
1. 从B模块需要的接口

def parse_story(story: str) -> List[Tuple]:
    """
    输入: "John went to the kitchen. The apple was missing."
    输出: [("enter", "john", "kitchen"), ("missing", "apple")]
    """
    pass

输出：List[Tuple]，每个Tuple是 (谓词, 参数1, 参数2, ...)

2. 从A模块需要的接口

def abduce(facts: List[Tuple]) -> List[Dict]:
    """
    输入: [("missing", "apple"), ("at", "john", "kitchen")]
    输出: [
        {
            "hypothesis": ("pick", "john", "apple"),
            "score": 0.95,
            "path": ["missing(apple)", "has(john,apple)", "pick(john,apple)"]
        },
        ...
    ]
    """
    pass

输出：List[Dict]，按score降序排列（最高分在前）

## D提供的接口
1. 主入口函数 - reason(story: str) -> Dict
def reason(story: str) -> Dict:
    """
    输入: 自然语言故事
    输出: 推理结果字典
    """
    pass