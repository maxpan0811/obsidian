# 四川省四大联盟华程双品牌预订市占率分析工具 — 实现计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task.

**Goal:** 创建分析四川省四大门店联盟（叮叮/周一/北斗/悠途）在上个自然周的华程双品牌预订市占率 Python 脚本，并注册为 Claude Code skill。

**Architecture:** 单脚本架构。内置四大联盟门店清单字典，脚本自动计算目标周/环比周/同比周起止日期，读取 2026/2025 两份携程订单 Excel，按门店名子串匹配分配到各联盟，聚合营收计算双品牌占比，输出 5-Sheet Excel（1 汇总 + 4 联盟明细）。

**Tech Stack:** Python 3.12+，openpyxl（读写 Excel），datetime/calendar（周计算），标准库 collections（defaultdict 聚合）

---

## 文件结构

```
/Users/panbo/.claude/skills/四川省联盟市占率分析工具/
├── SKILL.md                              # 技能定义 —— 触发器、用法说明、配置参数
└── scripts/
    └── analyze_alliance_share.py         # 主分析脚本 —— 全部业务逻辑
```

## 脚本设计

### 常量与配置（脚本顶部，一处修改）

```python
DATA_DIR        = "/Users/panbo/Documents/artnova"
ORDERS_FILE_2026 = None      # None = 自动匹配最新
ORDERS_FILE_2025 = None      # None = 自动匹配最新
TARGET_WEEK      = None      # None = 自动检测上周
TARGET_YEAR      = 2026
REGION_FILTER    = "欧洲"

# 列号（1-based，从表头读取确认）
COL_REGION   = 2     # 目的地国家_归属业务板块
COL_ORDER_DT = 13    # 下单日期
COL_PROD_ID  = 26    # 产品id
COL_PROD_NM  = 27    # 下单时产品名称
COL_STORE    = 31    # 门店名称
COL_SUPPLIER = 41    # 供应商名称
COL_BRAND    = 60    # 订单归属
COL_REVENUE  = 74    # 成交收入
COL_PEOPLE   = 75    # 成交人数
```

### 门店清单

```python
# 每个联盟一个列表，每条: {品牌, 名称, 对接销售}
# 四个联盟合计约 69 家门店
ALLIANCE_STORES = {
    "叮叮旅游": [ ... 12 家 ... ],
    "周一联盟": [ ... 30 家 ... ],
    "北斗联盟": [ ... 8 家 ... ],
    "悠途联盟": [ ... 19 家 ... ],
}
# 特殊门店名映射（原名 -> 订单中实际全名字串）
SPECIAL_STORE_MAP = {"名山县门市": "雅安携程名山区名山门市"}
```

### 核心函数

| 函数 | 行数 | 职责 |
|------|------|------|
| `calculate_week_ranges(now=None)` | ~30 | 计算目标周/环比周/同比周的 `(start, end)` 日期范围 |
| `find_latest_file(dir_path, pattern)` | ~10 | 找目录下最新匹配文件 |
| `load_orders(filepath, start_date, end_date, region)` | ~40 | 读取订单 Excel，筛选业务板块和时间范围，返回列表 of dict |
| `match_store_to_alliance(store_name)` | ~15 | 短名子串匹配到各联盟门店，返回 `(联盟名, 门店信息)` 或 None |
| `calc_top_suppliers(orders_list, limit=3)` | ~15 | 按营收算 TOP3 供应商及占比 |
| `build_summary_sheet(...)` | ~50 | 构建 Sheet1 联盟汇总 |
| `build_alliance_sheet(...)` | ~80 | 构建 Sheet2-5 各联盟门店明细 |
| `create_excel(period_data, output_path)` | ~100 | 组装整个 Excel 文件 |
| `main()` | ~30 | 入口：时间计算 → 加载订单 → 聚合 → 生成 Excel |

---

### Task 1: 创建技能目录和 SKILL.md

**Files:**
- Create: `/Users/panbo/.claude/skills/四川省联盟市占率分析工具/SKILL.md`

- [ ] **Step 1: 创建目录**

```bash
mkdir -p "/Users/panbo/.claude/skills/四川省联盟市占率分析工具/scripts"
```

- [ ] **Step 2: 写 SKILL.md**

内容包含：
- name/description/trigger 三字段 frontmatter
- 触发词：联盟市占率、四大联盟、叮叮旅游、周一联盟、北斗联盟、悠途联盟
- 数据源路径说明（订单文件、门店清单内置）
- 用法：`cd [skill_dir] && python3 scripts/analyze_alliance_share.py`
- 可配置参数清单
- 输出文件命名规则
- 注意事项（门店清单更新方式、同比需要 2025 文件）

- [ ] **Step 3: 提交（git add + commit）**

---

### Task 2: 写时间范围计算模块

**Files:**
- Create: `/Users/panbo/.claude/skills/四川省联盟市占率分析工具/scripts/analyze_alliance_share.py`（依次追加代码）

- [ ] **Step 1: 在脚本中实现 `calculate_week_ranges()` 函数**

```python
from datetime import datetime, timedelta
import calendar

def calculate_week_ranges(now=None):
    """返回目标周/环比周/同比周的起止日期 (start, end) 元组。
    
    目标周 = 上一个完整的自然周（周一 ~ 周日）
    环比周 = 目标周的前一周
    同比周 = 去年同一周编号的日期范围
    
    Returns:
        dict: {
            "target": (datetime, datetime),
            "prev": (datetime, datetime),
            "yoy": (datetime, datetime),
        }
    """
    if now is None:
        now = datetime.now()
    
    # 找到上周一的 00:00:00
    days_since_monday = now.weekday()  # Monday=0
    last_monday = now - timedelta(days=days_since_monday + 7)
    target_start = last_monday.replace(hour=0, minute=0, second=0, microsecond=0)
    target_end = (target_start + timedelta(days=7)).replace(microsecond=0) - timedelta(microseconds=1)
    
    # 环比 = 再往前一周
    prev_start = target_start - timedelta(days=7)
    prev_end = target_start - timedelta(microseconds=1)
    
    # 同比：去年同周编号
    target_iso_week = target_start.isocalendar()[1]
    yoy_start = target_start.replace(year=target_start.year - 1)
    # 找去年同样 ISO 周编号的周一
    yoy_start = yoy_start - timedelta(days=yoy_start.weekday())
    yoy_end = (yoy_start + timedelta(days=7)).replace(microsecond=0) - timedelta(microseconds=1)
    
    return {
        "target": (target_start, target_end),
        "prev": (prev_start, prev_end),
        "yoy": (yoy_start, yoy_end),
        "iso_week": target_iso_week,
        "year": target_start.year,
    }
```

验证逻辑：如果今天是 2026-06-13（周六），target_start 应该是 2026-06-01（周一）还是 2026-06-08（周一）？  
- weekday() 返回 Monday=0, Saturday=5  
- days_since_monday = 5  
- last_monday = 6/13 - (5+7) = 6/13 - 12 = 6/1 → ❌ 这是大上周一  
- 应该是：target_start = last_monday + timedelta(days=7) = 6/1 + 7 = 6/8 ✅

所以修正：`days_since_monday + 7` 会多减一周。正确写法：

```python
days_since_monday = now.weekday()  # 0=Mon..6=Sun
days_to_last_monday = days_since_monday + 7  # 到上周一
last_monday = (now - timedelta(days=days_to_last_monday)).replace(
    hour=0, minute=0, second=0, microsecond=0)
target_start = last_monday
target_end = (target_start + timedelta(days=7)) - timedelta(microseconds=1)
```

- [ ] **Step 2: 添加日期格式化辅助函数**

```python
def fmt_date_range(start, end):
    """返回可读的日期范围字符串，如 '6/8(一)-6/14(日)'"""
    weekdays_cn = ["一", "二", "三", "四", "五", "六", "日"]
    return f"{start.month}/{start.day}({weekdays_cn[start.weekday()]})-{end.month}/{end.day}({weekdays_cn[end.weekday()]})"
```

- [ ] **Step 3: 用以下代码手动验证时间计算（运行后打印结果，视觉确认）**

```python
if __name__ == "__main__":
    ranges = calculate_week_ranges()
    for k, v in ranges.items():
        if isinstance(v, tuple):
            print(f"{k}: {v[0]} -> {v[1]}")
        else:
            print(f"{k}: {v}")
```

预期的正确输出（如果 2026-06-13 运行）：
```
target: 2026-06-08 00:00:00 -> 2026-06-14 23:59:59.999999
prev: 2026-06-01 00:00:00 -> 2026-06-07 23:59:59.999999
yoy: 2025-06-09 00:00:00 -> 2025-06-15 23:59:59.999999
```

---

### Task 3: 门店清单与匹配模块

**Files:**
- Modify: `scripts/analyze_alliance_share.py`

- [ ] **Step 1: 添加四大联盟门店清单常量**

```python
ALLIANCE_STORES = {
    "叮叮旅游": [
        {"brand": "百事通", "name": "武侯区双楠街门市", "contact": "王越凡"},
        {"brand": "携程", "name": "成华区双桥路门市", "contact": "王越凡"},
        {"brand": "百事通", "name": "金牛区李家沱门市", "contact": "王越凡"},
        {"brand": "百事通", "name": "青羊区财大北门门市", "contact": "王越凡"},
        {"brand": "百事通", "name": "武侯区大石东路门市", "contact": "王越凡"},
        {"brand": "百事通", "name": "成华区建设路门市", "contact": "王越凡"},
        {"brand": "百事通", "name": "金牛区银沙路门市", "contact": "王越凡"},
        {"brand": "百事通", "name": "锦江区莲花小区门市", "contact": "王越凡"},
        {"brand": "百事通", "name": "金牛区蜀汉路门市", "contact": "李涛"},
        {"brand": "去哪儿", "name": "武侯区高新区肖家河中街门市", "contact": "王越凡"},
        {"brand": "百事通", "name": "武侯区高新区玉林南路门市", "contact": "王越凡"},
        {"brand": "去哪儿", "name": "金牛区永陵路门市", "contact": "王越凡"},
    ],
    "周一联盟": [
        {"brand": "携程", "name": "武侯区高新区阳光街门市", "contact": "李涛"},
        {"brand": "携程", "name": "武侯区航空路门市", "contact": "吴金龙"},
        {"brand": "携程", "name": "武侯区高新区锦城大道门市", "contact": "李涛"},
        {"brand": "携程", "name": "武侯区来凤三路第一门市", "contact": "吴金龙"},
        {"brand": "携程", "name": "武侯区高新区和硕西街门市", "contact": "史琪"},
        {"brand": "携程", "name": "武侯区高新区天久南巷门市", "contact": "李涛"},
        {"brand": "携程", "name": "武侯区丽都路门市", "contact": "史琪"},
        {"brand": "携程", "name": "成华区东风路门市", "contact": "史琪"},
        {"brand": "携程", "name": "金牛区沙湾东一路门市", "contact": "李涛"},
        {"brand": "携程", "name": "青羊区光华西三路金地自在湾门市", "contact": "吴金龙"},
        {"brand": "百事通", "name": "青羊区草市街门市", "contact": "史琪"},
        {"brand": "携程", "name": "成华区一环路东一段门市", "contact": "李涛"},
        {"brand": "携程", "name": "武侯区人民南路门市", "contact": "史琪"},
        {"brand": "携程", "name": "成华区双福一路门市", "contact": "李涛"},
        {"brand": "携程", "name": "武侯区高新区天府二街鹭洲里门市", "contact": "李涛"},
        {"brand": "携程", "name": "名山县门市", "contact": "陶义娟/史琪"},
        {"brand": "携程", "name": "崇州蜀州中路宫保里门市", "contact": "李涛"},
        {"brand": "去哪儿", "name": "武侯区高新区肖家河中街门市", "contact": "王越凡"},
        {"brand": "携程", "name": "温江区御景湾门市", "contact": "史琪"},
        {"brand": "去哪儿", "name": "金牛区永陵路门市", "contact": "王越凡"},
        {"brand": "携程", "name": "青羊区蜀江路门市", "contact": "史琪"},
        {"brand": "携程", "name": "温江区文化路门市", "contact": "史琪"},
        {"brand": "携程", "name": "双流区麓山大道和悦广场门市", "contact": "吴金龙"},
        {"brand": "携程", "name": "郫都区科化二路门市", "contact": "史琪"},
        {"brand": "携程", "name": "锦江区枫树街卓锦曼购门市", "contact": "李涛"},
        {"brand": "携程", "name": "新都区桂水路门市", "contact": "史琪"},
        {"brand": "百事通", "name": "金牛区抚琴门市", "contact": "史琪"},
        {"brand": "携程", "name": "金牛区金科南三路门市", "contact": "李涛"},
        {"brand": "携程", "name": "金牛区抚琴路门市", "contact": "史琪"},
        {"brand": "携程", "name": "双流区华阳美岸路门市", "contact": "李涛"},
    ],
    "北斗联盟": [
        {"brand": "携程", "name": "都江堰新马路门市", "contact": "吴金龙"},
        {"brand": "百事通", "name": "双流区海昌路门市", "contact": "王思思"},
        {"brand": "携程", "name": "武侯区高新区神仙树南路门市", "contact": "王思思"},
        {"brand": "百事通", "name": "金牛区西体路门市", "contact": "王思思"},
        {"brand": "百事通", "name": "武侯区中华锦绣门市", "contact": "王思思"},
        {"brand": "携程", "name": "郫都区国宁东路门市", "contact": "王思思"},
        {"brand": "百事通", "name": "金牛区营门口第二门市", "contact": "王思思"},
        {"brand": "百事通", "name": "金牛区马鞍街门市", "contact": "王思思"},
    ],
    "悠途联盟": [
        {"brand": "携程", "name": "锦江区莲花北路门市", "contact": "吴金龙"},
        {"brand": "百事通", "name": "锦江区翡翠城二期门市", "contact": "吴金龙"},
        {"brand": "携程", "name": "青羊区青华路门市", "contact": "吴金龙"},
        {"brand": "携程", "name": "高新区紫荆东路门市", "contact": "吴金龙"},
        {"brand": "携程", "name": "成华区杉板桥滨江天街门市", "contact": "陶义娟"},
        {"brand": "携程", "name": "武侯区星悦路门市", "contact": "吴金龙"},
        {"brand": "携程", "name": "成华区建兴路门市", "contact": "吴金龙"},
        {"brand": "携程", "name": "青羊区德盛路门市", "contact": "王思思"},
        {"brand": "百事通", "name": "青羊区网络营销中心销售26部门市", "contact": "吴金龙"},
        {"brand": "携程", "name": "南充携程顺庆区北湖公园门市", "contact": "吴金龙"},
        {"brand": "携程", "name": "成华区府青路二段门市", "contact": "吴金龙"},
        {"brand": "百事通", "name": "武侯区五大花园门市", "contact": "吴金龙"},
        {"brand": "携程", "name": "武侯区新裕路天目中心门市", "contact": "吴金龙"},
        {"brand": "携程", "name": "青羊区黄田坝门市", "contact": "吴金龙"},
        {"brand": "百事通", "name": "金牛区九里堤北门市", "contact": "吴金龙"},
        {"brand": "百事通", "name": "青羊区网络营销中心销售33部门市", "contact": "吴金龙"},
        {"brand": "携程", "name": "青羊区瑞联路门市", "contact": "吴金龙"},
        {"brand": "携程", "name": "成华区东丽街门市", "contact": "吴金龙"},
        {"brand": "携程", "name": "大邑南街门市", "contact": "王思思"},
    ],
}

# 特殊门店名映射（短名 -> 订单系统中的全名含有的子串）
SPECIAL_STORE_MAP = {
    "名山县门市": "雅安携程名山区名山门市",
}
```

- [ ] **Step 2: 添加 `match_store_to_alliance()` 函数**

```python
def match_store_to_alliance(store_name):
    """将订单完整门店名匹配到联盟门店短名。
    
    返回: (联盟名, 门店信息 dict) 或 None
    """
    if not store_name:
        return None
    name_clean = store_name.strip()
    
    for alliance_name, stores in ALLIANCE_STORES.items():
        for store_info in stores:
            short_name = store_info["name"]
            # 检查特殊映射
            effective_short = SPECIAL_STORE_MAP.get(short_name, short_name)
            if effective_short in name_clean:
                return (alliance_name, store_info)
    return None
```

- [ ] **Step 3: 添加 `find_latest_file()` 和 `get_order_files()` 函数**

```python
import glob

def find_latest_file(directory, pattern):
    """在目录中找到最新匹配的文件名（基于日期后缀或修改时间）"""
    full_pattern = os.path.join(directory, pattern)
    files = glob.glob(full_pattern)
    if not files:
        return None
    # 按修改时间降序取最新
    return max(files, key=os.path.getmtime)

def get_order_files(data_dir, year_2026_pattern, year_2025_pattern):
    """自动匹配或使用手动指定的文件路径"""
    fp_2026 = ORDERS_FILE_2026
    fp_2025 = ORDERS_FILE_2025
    
    if fp_2026 is None:
        fp_2026 = find_latest_file(data_dir, year_2026_pattern)
    else:
        fp_2026 = os.path.join(data_dir, fp_2026) if not os.path.isabs(fp_2026) else fp_2026
    
    if fp_2025 is None:
        fp_2025 = find_latest_file(data_dir, year_2025_pattern)
    else:
        fp_2025 = os.path.join(data_dir, fp_2025) if not os.path.isabs(fp_2025) else fp_2025
    
    return fp_2026, fp_2025
```

---

### Task 4: 订单加载和数据聚合函数

**Files:**
- Modify: `scripts/analyze_alliance_share.py`

- [ ] **Step 1: 实现 `load_orders()` 函数**

```python
from collections import defaultdict
import openpyxl

def load_orders(filepath, region, start_date, end_date):
    """加载订单Excel，筛选业务板块和时间范围（下单日期）。
    
    Returns: list of dict, each with keys:
        store_name, revenue, people, supplier, brand_tag, order_date
    """
    if not filepath or not os.path.exists(filepath):
        print(f"  ⚠️ 文件不存在: {filepath}")
        return []
    
    wb = openpyxl.load_workbook(filepath, read_only=True, data_only=True)
    ws = wb.active
    
    orders = []
    total_rows = 0
    matched_rows = 0
    
    for row in ws.iter_rows(values_only=True):
        total_rows += 1
        if total_rows == 1:
            continue  # 跳过表头
        
        region_val = str(row[COL_REGION - 1] or "").strip()
        if region not in region_val:
            continue
        
        # 下单日期筛选
        order_date = row[COL_ORDER_DT - 1]
        if order_date is None:
            continue
        
        # 处理日期格式：Excel serial 或 datetime
        if isinstance(order_date, (int, float)):
            from datetime import datetime as dt
            order_dt = dt.fromordinal(dt(1900, 1, 1).toordinal() + int(order_date) - 2)
        elif isinstance(order_date, datetime):
            order_dt = order_date
        else:
            try:
                order_dt = datetime.strptime(str(order_date).strip(), "%Y-%m-%d")
            except ValueError:
                continue
        
        # 必须在目标周期内
        if not (start_date <= order_dt <= end_date):
            continue
        
        store_name = str(row[COL_STORE - 1] or "").strip() if row[COL_STORE - 1] else ""
        revenue = float(row[COL_REVENUE - 1]) if row[COL_REVENUE - 1] else 0
        people = int(row[COL_PEOPLE - 1]) if row[COL_PEOPLE - 1] else 0
        brand_tag = str(row[COL_BRAND - 1] or "").strip()
        supplier = str(row[COL_SUPPLIER - 1] or "").strip() if row[COL_SUPPLIER - 1] else ""
        
        orders.append({
            "store_name": store_name,
            "revenue": revenue,
            "people": people,
            "supplier": supplier,
            "brand_tag": brand_tag,
            "order_date": order_dt,
        })
        matched_rows += 1
    
    wb.close()
    print(f"  📄 {os.path.basename(filepath)}: 总行 {total_rows-1}, 匹配 {matched_rows} 条订单")
    return orders
```

- [ ] **Step 2: 实现品牌分类和门店聚合函数**

```python
HUACHENG_KEYWORDS = ["华程", "账号订单"]
GUO_LV_KEYWORD = "国旅订单"

def classify_brand(brand_tag):
    """返回 'huacheng' / 'guolv' / 'other'"""
    if GUO_LV_KEYWORD in brand_tag:
        return "guolv"
    if any(kw in brand_tag for kw in HUACHENG_KEYWORDS):
        return "huacheng"
    return "other"

def aggregate_store_orders(orders):
    """按门店聚合营收数据。
    
    Returns: dict of {store_name: {total_rev, hc_rev, gl_rev, total_people, count, 
                                     suppliers: {name: revenue}}}
    """
    agg = defaultdict(lambda: {
        "total_rev": 0.0, "hc_rev": 0.0, "gl_rev": 0.0,
        "total_people": 0, "count": 0, "suppliers": defaultdict(float),
    })
    
    for o in orders:
        store = o["store_name"]
        if not store:
            continue
        brand = classify_brand(o["brand_tag"])
        agg[store]["total_rev"] += o["revenue"]
        agg[store]["total_people"] += o["people"]
        agg[store]["count"] += 1
        if brand == "huacheng":
            agg[store]["hc_rev"] += o["revenue"]
        elif brand == "guolv":
            agg[store]["gl_rev"] += o["revenue"]
        if o["supplier"]:
            agg[store]["suppliers"][o["supplier"]] += o["revenue"]
    
    return dict(agg)

def calc_top_suppliers(suppliers_dict, limit=3):
    """从供应商营收字典返回 TOP N [(name, revenue, pct), ...]"""
    sorted_s = sorted(suppliers_dict.items(), key=lambda x: -x[1])
    total = sum(suppliers_dict.values()) if suppliers_dict else 1
    result = []
    for name, rev in sorted_s[:limit]:
        result.append((name, rev, rev / total * 100 if total else 0))
    return result
```

- [ ] **Step 3: 实现 `process_alliance_orders()` 主聚合逻辑**

```python
def process_alliance_orders(orders, period_name=""):
    """将订单分配到各联盟门店，计算每家门店的双品牌指标。
    
    Returns:
        dict {联盟名: {
            "stores": [(store_info, metrics_dict, top_suppliers), ...],
            "summary": {total_rev, hc_rev, gl_rev, total_people, count, store_count, active_store_count}
        }}
    """
    # 先聚合订单
    store_agg = aggregate_store_orders(orders)
    
    # 匹配到联盟门店
    alliance_data = {}
    for alliance_name, stores in ALLIANCE_STORES.items():
        alliance_stores = []
        summary = {"total_rev": 0.0, "hc_rev": 0.0, "gl_rev": 0.0,
                    "total_people": 0, "count": 0, 
                    "store_count": len(stores), "active_store_count": 0}
        
        for store_info in stores:
            short_name = store_info["name"]
            effective_name = SPECIAL_STORE_MAP.get(short_name, short_name)
            
            # 在聚合数据中找匹配的订单
            matched_rev = 0.0
            matched_hc = 0.0
            matched_gl = 0.0
            matched_people = 0
            matched_count = 0
            matched_suppliers = {}
            
            for order_store, data in store_agg.items():
                if effective_name in order_store:
                    matched_rev += data["total_rev"]
                    matched_hc += data["hc_rev"]
                    matched_gl += data["gl_rev"]
                    matched_people += data["total_people"]
                    matched_count += data["count"]
                    for s, r in data["suppliers"].items():
                        matched_suppliers[s] = matched_suppliers.get(s, 0) + r
            
            metrics = {
                "total_rev": matched_rev,
                "hc_rev": matched_hc,
                "gl_rev": matched_gl,
                "dual_pct": (matched_hc + matched_gl) / matched_rev * 100 if matched_rev > 0 else 0.0,
                "people": matched_people,
                "count": matched_count,
            }
            top_s = calc_top_suppliers(matched_suppliers)
            
            alliance_stores.append((store_info, metrics, top_s))
            
            # 汇总
            summary["total_rev"] += matched_rev
            summary["hc_rev"] += matched_hc
            summary["gl_rev"] += matched_gl
            summary["total_people"] += matched_people
            summary["count"] += matched_count
            if matched_count > 0:
                summary["active_store_count"] += 1
        
        # 按营收降序排列门店
        alliance_stores.sort(key=lambda x: -x[1]["total_rev"])
        alliance_data[alliance_name] = {"stores": alliance_stores, "summary": summary}
    
    return alliance_data
```

---

### Task 5: Excel 输出——样式定义和 Sheet1 汇总

**Files:**
- Modify: `scripts/analyze_alliance_share.py`

- [ ] **Step 1: 定义样式常量**

```python
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side, numbers
from openpyxl.utils import get_column_letter

# 字体
FONT_HEADER = Font(name="微软雅黑", size=10, bold=True, color="FFFFFF")
FONT_NORMAL = Font(name="微软雅黑", size=10)
FONT_TITLE = Font(name="微软雅黑", size=12, bold=True)

# 填充
FILL_HEADER = PatternFill("solid", fgColor="1F4E79")
FILL_HEADER_SUB = PatternFill("solid", fgColor="2E75B6")
FILL_EVEN = PatternFill("solid", fgColor="E8F0FE")
FILL_SUMMARY = PatternFill("solid", fgColor="1F4E79")
FILL_UP = PatternFill("solid", fgColor="C6EFCE")    # 绿色上升
FILL_DOWN = PatternFill("solid", fgColor="FFC7CE")  # 红色下降
FILL_ORANGE = PatternFill("solid", fgColor="FCE4D6") # 浅橘TOP1非华程

# 对齐
ALIGN_CENTER = Alignment(horizontal="center", vertical="center", wrap_text=True)
ALIGN_RIGHT = Alignment(horizontal="right", vertical="center")
ALIGN_LEFT = Alignment(horizontal="left", vertical="center")

# 边框
THIN_BORDER = Border(
    left=Side(style="thin"), right=Side(style="thin"),
    top=Side(style="thin"), bottom=Side(style="thin"),
)

# 数字格式
FMT_INT = '#,##0'
FMT_PCT = '0.00%'
```

- [ ] **Step 2: 实现 `create_summary_sheet()`**

```python
def create_summary_sheet(wb, alliance_data, week_ranges):
    """创建 Sheet1: 联盟汇总对比"""
    ws = wb.active
    ws.title = "联盟汇总对比"
    
    # 标题行
    target_start, target_end = week_ranges["target"]
    date_str = f"{target_start.year}年第{week_ranges['iso_week']}周 ({fmt_date_range(target_start, target_end)})"
    ws.merge_cells("A1:M1")
    ws["A1"] = f"四川省四大联盟华程双品牌预订市占率分析 ┊ {date_str}"
    ws["A1"].font = FONT_TITLE
    
    # 表头
    headers = ["联盟", "门店数", "有订单门店", "订单数", "人数", "总营收",
               "华程收入", "国旅收入", "本周双品牌占比", "上周双品牌占比", 
               "环比变化", "2025同周占比", "同比变化"]
    
    for col, h in enumerate(headers, 1):
        cell = ws.cell(2, col, h)
        cell.font = FONT_HEADER
        cell.fill = FILL_HEADER
        cell.alignment = ALIGN_CENTER
        cell.border = THIN_BORDER
    
    # 数据行
    for row_idx, (alliance_name, data) in enumerate(alliance_data.items(), 3):
        s = data["summary"]
        dual_pct = s["hc_rev"] + s["gl_rev"] / s["total_rev"] if s["total_rev"] > 0 else 0
        
        row_data = [
            alliance_name,
            s["store_count"],
            s["active_store_count"],
            s["count"],
            s["total_people"],
            s["total_rev"],
            s["hc_rev"],
            s["gl_rev"],
            dual_pct,
        ]
        # 环比数据和同比数据需要从外部传入（后面步骤补充）
        # 目前先填充占位
    
    # 列宽
    col_widths = [14, 8, 10, 8, 8, 12, 12, 12, 14, 14, 10, 14, 10]
    for i, w in enumerate(col_widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w
    
    # 冻结表头
    ws.freeze_panes = "A3"
```

BUT — 环比和同比数据需要跨周期比较，所以 `create_summary_sheet()` 不能只取本周数据，需要三个周期的 `alliance_data`。

修正设计：收集三个周期的alliance数据后再调用。

---

### Task 6: Excel 输出——Sheet2-5 各联盟门店明细

**Files:**
- Modify: `scripts/analyze_alliance_share.py`

- [ ] **Step 1: 实现 `create_alliance_sheet()`**

```python
def create_alliance_sheet(wb, alliance_name, stores_with_metrics, 
                           prev_data=None, yoy_data=None, week_ranges=None):
    """创建一个联盟的门店明细 Sheet。
    
    stores_with_metrics: [(store_info, metrics, top_suppliers), ...] 按营收降序
    prev_data: 环比周期的 {store_name -> metrics} 用于填充上周占比
    yoy_data: 同比周期的同上
    """
    ws = wb.create_sheet(title=f"{alliance_name}")
    
    # 标题
    ws.merge_cells("A1:O1")
    ws["A1"] = f"{alliance_name} ┊ {fmt_date_range(week_ranges['target'][0], week_ranges['target'][1])} 预订市占率"
    ws["A1"].font = FONT_TITLE
    
    # 表头
    headers = ["排名", "品牌", "门店", "对接销售", "本周单数", "本周人数", "本周营收",
               "华程收入", "国旅收入", "本周双品牌占比", "上周双品牌占比", 
               "同比双品牌占比", "TOP1供应商", "TOP2供应商", "TOP3供应商"]
    
    for col, h in enumerate(headers, 1):
        cell = ws.cell(2, col, h)
        cell.font = FONT_HEADER
        cell.fill = FILL_HEADER
        cell.alignment = ALIGN_CENTER
        cell.border = THIN_BORDER
    
    # 数据行
    for row_idx, (store_info, metrics, top_s) in enumerate(stores_with_metrics, 3):
        rank = row_idx - 2
        brand = store_info["brand"]
        store_name = store_info["name"]
        contact = store_info["contact"] or ""
        
        # 查找上周和同比数据
        prev_dual = None
        yoy_dual = None
        if prev_data and store_name in prev_data:
            prev_metrics = prev_data[store_name]
            prev_dual = prev_metrics.get("dual_pct")
        if yoy_data and store_name in yoy_data:
            yoy_metrics = yoy_data[store_name]
            yoy_dual = yoy_metrics.get("dual_pct")
        
        # 供应商字符串
        def supplier_str(s, idx):
            if idx < len(s):
                name, rev, pct = s[idx]
                return f"{name}({pct:.1f}%)"
            return "-"
        
        row_values = [
            rank, brand, store_name, contact,
            metrics["count"], metrics["people"], metrics["total_rev"],
            metrics["hc_rev"], metrics["gl_rev"],
            metrics["dual_pct"] / 100 if metrics["total_rev"] > 0 else 0,
            prev_dual / 100 if prev_dual is not None else "-",
            yoy_dual / 100 if yoy_dual is not None else "-",
            supplier_str(top_s, 0), supplier_str(top_s, 1), supplier_str(top_s, 2),
        ]
        
        for col, val in enumerate(row_values, 1):
            cell = ws.cell(row_idx, col, val)
            cell.font = FONT_NORMAL
            cell.border = THIN_BORDER
            if col <= 4:
                cell.alignment = ALIGN_CENTER
            elif col >= 13:
                cell.alignment = ALIGN_LEFT
            else:
                cell.alignment = ALIGN_RIGHT
            
            # 数值格式
            if col in (5, 6):
                cell.number_format = FMT_INT
            elif col in (7, 8, 9):
                cell.number_format = FMT_INT
            elif col in (10, 11, 12) and isinstance(val, float):
                cell.number_format = FMT_PCT
        
        # 条件格式：偶数行浅蓝
        if row_idx % 2 == 0:
            for col in range(1, 16):
                ws.cell(row_idx, col).fill = FILL_EVEN
        
        # TOP1 非华程 => 整行浅橘
        if top_s and top_s[0][0] and "华程" not in top_s[0][0]:
            for col in range(1, 16):
                ws.cell(row_idx, col).fill = FILL_ORANGE
        
        # 本周 vs 上周 占比变化的颜色标记（列10 = 本周，列11 = 上周）
        cell_this = ws.cell(row_idx, 10)
        cell_prev = ws.cell(row_idx, 11)
        if isinstance(cell_this.value, float) and isinstance(cell_prev.value, float):
            if cell_this.value > cell_prev.value:
                cell_this.fill = FILL_UP
            elif cell_this.value < cell_prev.value:
                cell_this.fill = FILL_DOWN
    
    # 合计行
    total_row = len(stores_with_metrics) + 3
    ws.cell(total_row, 1, "合计").font = Font(name="微软雅黑", size=10, bold=True, color="FFFFFF")
    for col in range(1, 16):
        c = ws.cell(total_row, col)
        c.fill = FILL_SUMMARY
        c.font = Font(name="微软雅黑", size=10, bold=True, color="FFFFFF")
        c.border = THIN_BORDER
    
    # 列宽
    col_widths = [6, 8, 28, 12, 8, 8, 12, 12, 12, 14, 14, 14, 24, 24, 24]
    for i, w in enumerate(col_widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w
    
    ws.freeze_panes = "A3"
    return ws
```

---

### Task 7: 主流程协调

**Files:**
- Modify: `scripts/analyze_alliance_share.py`

- [ ] **Step 1: 实现 `main()` 函数**

```python
def main():
    print("=" * 60)
    print("  四川省四大联盟华程双品牌预订市占率分析")
    print("=" * 60)
    
    # 1. 时间范围
    week_ranges = calculate_week_ranges()
    print(f"\n📅 目标周: {fmt_date_range(*week_ranges['target'])} (第{week_ranges['iso_week']}周)")
    print(f"📅 环比周: {fmt_date_range(*week_ranges['prev'])}")
    print(f"📅 同比周: {fmt_date_range(*week_ranges['yoy'])}")
    
    # 2. 文件路径
    fp_2026, fp_2025 = get_order_files(DATA_DIR, 
        "2026年1-12月携程渠道海外跟团游订单明细(自营&代理)*.xlsx",
        "2025年1-12月携程渠道海外跟团游订单明细(自营&代理)*.xlsx")
    
    if not fp_2026:
        print("❌ 找不到 2026 年订单文件!")
        return
    print(f"\n📁 2026: {os.path.basename(fp_2026)}")
    print(f"📁 2025: {os.path.basename(fp_2025) if fp_2025 else '未找到'}")
    
    # 3. 加载订单（三个周期）
    region = REGION_FILTER
    
    # 本周
    print("\n🔍 加载本周数据...")
    orders_target = load_orders(fp_2026, region, *week_ranges["target"])
    target_data = process_alliance_orders(orders_target, "本周")
    
    # 环比上周
    print("\n🔍 加载环比数据...")
    orders_prev = load_orders(fp_2026, region, *week_ranges["prev"])
    prev_data = process_alliance_orders(orders_prev, "上周")
    
    # 同比去年
    orders_yoy = []
    yoy_data = None
    if fp_2025:
        print("\n🔍 加载同比数据...")
        orders_yoy = load_orders(fp_2025, region, *week_ranges["yoy"])
        yoy_data = process_alliance_orders(orders_yoy, "去年同周")
    else:
        print("\n⚠️ 跳过同比（2025文件不存在）")
    
    # 4. 创建 Excel
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_name = f"2026年第{week_ranges['iso_week']}周四川省四大联盟华程双品牌市占率分析{timestamp}.xlsx"
    output_path = os.path.join(DATA_DIR, output_name)
    
    print(f"\n📊 生成报表: {output_name}")
    wb = openpyxl.Workbook()
    
    # 建立门店名 -> metrics 的查找字典（用于环比/同比）
    def build_store_lookup(data):
        lookup = {}
        for aname, adata in data.items():
            for store_info, metrics, _ in adata["stores"]:
                lookup[store_info["name"]] = metrics
        return lookup
    
    prev_lookup = build_store_lookup(prev_data)
    yoy_lookup = build_store_lookup(yoy_data) if yoy_data else {}
    
    # Sheet1 汇总
    ws_summary = create_summary_sheet(wb, target_data, prev_data, yoy_data, week_ranges, prev_lookup, yoy_lookup)
    
    # Sheet2-5 各联盟
    for alliance_name in ["叮叮旅游", "周一联盟", "北斗联盟", "悠途联盟"]:
        if alliance_name in target_data:
            stores = target_data[alliance_name]["stores"]
            create_alliance_sheet(wb, alliance_name, stores, prev_lookup, yoy_lookup, week_ranges)
    
    wb.save(output_path)
    print(f"\n✅ 报表已保存: {output_path}")
    
    # 5. 打印摘要
    print(f"\n📈 摘要 (第{week_ranges['iso_week']}周 预订口径):")
    print(f"{'联盟':<8} {'本周占比':>10} {'上周':>10} {'变化':>8} {'去年同周':>10}")
    print("-" * 50)
    for aname in ["叮叮旅游", "周一联盟", "北斗联盟", "悠途联盟"]:
        if aname in target_data:
            s = target_data[aname]["summary"]
            dual = (s["hc_rev"] + s["gl_rev"]) / s["total_rev"] * 100 if s["total_rev"] > 0 else 0
            prev_dual = None
            if aname in prev_data:
                ps = prev_data[aname]["summary"]
                prev_dual = (ps["hc_rev"] + ps["gl_rev"]) / ps["total_rev"] * 100 if ps["total_rev"] > 0 else 0
            
            yoy_dual = None
            if yoy_data and aname in yoy_data:
                ys = yoy_data[aname]["summary"]
                yoy_dual = (ys["hc_rev"] + ys["gl_rev"]) / ys["total_rev"] * 100 if ys["total_rev"] > 0 else 0
            
            delta = dual - prev_dual if prev_dual is not None else 0
            arrow = "↑" if delta > 0 else "↓"
            yoy_str = f"{yoy_dual:.1f}%" if yoy_dual is not None else "N/A"
            print(f"{aname:<8} {dual:>8.1f}% {prev_dual:>8.1f}% {arrow}{abs(delta):>5.1f}% {yoy_str:>10}")

if __name__ == "__main__":
    main()
```

- [ ] **Step 2: 补全 `create_summary_sheet()` 完整实现**

修正上面 Task 5 中的 `create_summary_sheet`，接收三个周期的数据：

```python
def create_summary_sheet(wb, target_data, prev_data, yoy_data, week_ranges, prev_lookup, yoy_lookup):
    """创建 Sheet1: 联盟汇总对比"""
    ws = wb.active
    ws.title = "联盟汇总对比"
    
    target_start, target_end = week_ranges["target"]
    date_str = f"{target_start.year}年第{week_ranges['iso_week']}周 ({fmt_date_range(target_start, target_end)})"
    
    # 标题
    ws.merge_cells("A1:M1")
    ws["A1"] = f"四川省四大联盟华程双品牌预订市占率分析 ┊ {date_str}"
    ws["A1"].font = FONT_TITLE
    
    # 表头
    headers = ["联盟", "门店数", "有订单门店", "订单数", "人数", "总营收",
               "华程收入", "国旅收入", "本周双品牌占比", "上周双品牌占比", 
               "环比变化", "2025同周占比", "同比变化"]
    for col, h in enumerate(headers, 1):
        cell = ws.cell(2, col, h)
        cell.font = FONT_HEADER
        cell.fill = FILL_HEADER
        cell.alignment = ALIGN_CENTER
        cell.border = THIN_BORDER
    
    # 数据
    for row_idx, aname in enumerate(["叮叮旅游", "周一联盟", "北斗联盟", "悠途联盟"], 3):
        if aname not in target_data:
            continue
        s = target_data[aname]["summary"]
        total = s["total_rev"]
        dual_pct = (s["hc_rev"] + s["gl_rev"]) / total if total > 0 else 0
        
        # 上周占比
        prev_dual_pct = None
        if aname in prev_data:
            ps = prev_data[aname]["summary"]
            pt = ps["total_rev"]
            prev_dual_pct = (ps["hc_rev"] + ps["gl_rev"]) / pt if pt > 0 else 0
        
        # 同比占比
        yoy_dual_pct = None
        if yoy_data and aname in yoy_data:
            ys = yoy_data[aname]["summary"]
            yt = ys["total_rev"]
            yoy_dual_pct = (ys["hc_rev"] + ys["gl_rev"]) / yt if yt > 0 else 0
        
        # 环比变化 = 本周 - 上周
        delta = (dual_pct - prev_dual_pct) if prev_dual_pct is not None else None
        yoy_delta = (dual_pct - yoy_dual_pct) if yoy_dual_pct is not None else None
        
        row_values = [
            aname, s["store_count"], s["active_store_count"],
            s["count"], s["total_people"], s["total_rev"],
            s["hc_rev"], s["gl_rev"],
            dual_pct,
            prev_dual_pct if prev_dual_pct is not None else "-",
            delta if delta is not None else "-",
            yoy_dual_pct if yoy_dual_pct is not None else "-",
            yoy_delta if yoy_delta is not None else "-",
        ]
        
        for col, val in enumerate(row_values, 1):
            cell = ws.cell(row_idx, col, val)
            cell.font = FONT_NORMAL
            cell.border = THIN_BORDER
            cell.alignment = ALIGN_CENTER if col <= 3 else ALIGN_RIGHT
            
            if col in (4, 5, 6, 7, 8):
                cell.number_format = FMT_INT
            elif col in (9, 10, 12) and isinstance(val, float):
                cell.number_format = FMT_PCT
            elif col in (11, 13):
                if isinstance(val, float):
                    cell.number_format = '+0.00%;-0.00%'
                else:
                    cell.alignment = ALIGN_CENTER
        
        # 颜色标记：环比上升绿、下降红
        cell_delta = ws.cell(row_idx, 11)
        if isinstance(cell_delta.value, float):
            if cell_delta.value > 0:
                cell_delta.fill = FILL_UP
            elif cell_delta.value < 0:
                cell_delta.fill = FILL_DOWN
        
        cell_yoy_delta = ws.cell(row_idx, 13)
        if isinstance(cell_yoy_delta.value, float):
            if cell_yoy_delta.value > 0:
                cell_yoy_delta.fill = FILL_UP
            elif cell_yoy_delta.value < 0:
                cell_yoy_delta.fill = FILL_DOWN
    
    # 合计行
    total_row = 7
    ws.cell(total_row, 1, "合计").font = Font(name="微软雅黑", size=10, bold=True, color="FFFFFF")
    for col in range(1, 14):
        c = ws.cell(total_row, col)
        c.fill = FILL_SUMMARY
        c.font = Font(name="微软雅黑", size=10, bold=True, color="FFFFFF")
        c.border = THIN_BORDER
    
    # 列宽
    col_widths = [14, 8, 10, 8, 8, 12, 12, 12, 14, 14, 10, 14, 10]
    for i, w in enumerate(col_widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w
    
    ws.freeze_panes = "A3"
    return ws
```

---

### Task 8: 整合脚本、运行验证

**Files:**
- Modify: `scripts/analyze_alliance_share.py`

- [ ] **Step 1: 把上面所有函数和配置按顺序整合到一个文件中**

完整的文件结构：

```
1. shebang + docstring
2. import 语句
3. 配置常量（DATA_DIR, 列号, 区域过滤等）
4. ALLIANCE_STORES 门店清单字典
5. SPECIAL_STORE_MAP 特殊映射
6. 样式常量（FONT_*, FILL_*, ALIGN_*, FMT_*）
7. calculate_week_ranges()
8. fmt_date_range()
9. find_latest_file() / get_order_files()
10. match_store_to_alliance()
11. classify_brand() / aggregate_store_orders() / calc_top_suppliers()
12. load_orders() / process_alliance_orders()
13. create_summary_sheet() / create_alliance_sheet()
14. main()
15. if __name__ == "__main__": main()
```

- [ ] **Step 2: 运行脚本验证**

```bash
cd "/Users/panbo/.claude/skills/四川省联盟市占率分析工具"
python3 scripts/analyze_alliance_share.py
```

预期输出：
- 打印时间范围、文件路径、加载行数
- 30 秒内完成，无报错
- 输出文件生成在 artnova 目录

- [ ] **Step 3: 核对输出文件**

```bash
ls -la /Users/panbo/Documents/artnova/*四大联盟*市占率* 2>/dev/null | tail -3
```

用 openpyxl 快速验证 Sheet 数量和行数（可选）：
```bash
python3 -c "
import openpyxl
fp = '/Users/panbo/Documents/artnova/2026年第23周四川省四大联盟华程双品牌市占率分析20260613.xlsx'
wb = openpyxl.load_workbook(fp)
print(f'Sheet 数: {len(wb.sheetnames)}')
for sn in wb.sheetnames:
    ws = wb[sn]
    print(f'  {sn}: {ws.max_row} 行 x {ws.max_column} 列')
wb.close()
"
```

---

### Task 9: 完善 SKILL.md 并提交

**Files:**
- Modify: `/Users/panbo/.claude/skills/四川省联盟市占率分析工具/SKILL.md`

- [ ] **Step 1: 完善 SKILL.md**

确保含以下内容：
- 完整的触发词清单
- 准确的数据源路径和列号引用
- 样例用法
- 门店清单更新指南
- 常见问题（同比文件不存在、门店匹配不到等）

- [ ] **Step 2: 最终验证**

重新跑一次完整流程，确保输出的 Excel 数据合理（而不是全 0 或全 100%）。

---

## 规格核对清单

| 规格要求 | 对应任务 |
|---------|---------|
| 四大联盟门店清单内置 | Task 3 |
| 预订口径（下单日期 Col 13） | Task 4 |
| 自然周自动计算 | Task 2 |
| 本周 + 环比 + 同比 | Task 7 main() |
| Sheet1 联盟汇总对比 | Task 7 |
| Sheet2-5 各联盟门店明细 | Task 6 |
| 按营收降序排列 | Task 4 process_alliance_orders() |
| 千分号/百分数/微软雅黑格式 | Task 5 样式常量 |
| 绿升红降条件格式 | Task 6 create_alliance_sheet() |
| 偶数行淡蓝 | Task 6 |
| TOP1 非华程浅橘 | Task 6 |
| 汇总行深蓝底白字 | Task 6 |
| SKILL.md 注册 | Task 1 + Task 9 |