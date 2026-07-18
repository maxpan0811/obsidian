---
title: 同期同比-and-national-yoy-implementation
type: capture
tags: [auto-capture, reference]
source: memory sync hook 2026-07-18
created: 2026-07-18
---


#同期同比与全国同比实现（2026-07-18）

## 核心概念

###同期同比定义
**同期同比** = 以相同的预定日期为截止点，对比不同年份的全年出发产量

例如：
- 2026年同期同比 = 2026年7月16日之前预定的 → 2026年全年出发的产量
- 2025年同期同比 = 2025年7月16日之前预定的 → 2025年全年出发的产量

### 数据字段区分
- **prod26**: 26年完成产量（截至7月16日，来自看板数据）
- **prod25**: 25年全年产量（用于显示"25年全年"列）
- **prod25_same**: 25年同期产量（截至7月16日，用于计算同期同比）
- **yoy**:同期同比增长率 = (prod26 - prod25_same) / prod25_same

## 实现细节

### 1. 数据提取（export_desktop.py）

```python
# 2025年数据：全年产量 +同期产量（截至7月16日）
from datetime import datetime
cutoff_date_2025 = datetime(2025, 7, 16)
order_sum_2025_full = defaultdict(float)  # 全年产量
order_sum_2025_same = defaultdict(float)  #同期产量（用于同比计算）

for o in orders_2025:
    cc = o.get('客户公司')
    amt = o.get('成交销售额')
    if cc and amt is not None and str(cc) not in SKIP_CUSTOMERS:
        order_date_str = o.get('下单日期')
        dep_date_str = o.get('出发日期')
        if order_date_str and dep_date_str:
            try:
                order_date = datetime.strptime(str(order_date_str)[:10], '%Y-%m-%d')
                dep_date = datetime.strptime(str(dep_date_str)[:10], '%Y-%m-%d')
                # 全年产量（所有2025年出发的订单）
                if dep_date.year == 2025:
                    order_sum_2025_full[str(cc)] += float(amt) / 10000
                #同期产量（下单日期 <= 2025-07-16 且出发日期在2025年）
                if order_date <= cutoff_date_2025 and dep_date.year == 2025:
                    order_sum_2025_same[str(cc)] += float(amt) / 10000
            except (ValueError, TypeError):
                pass
```

### 2. 数据结构

```python
rec = {
    '客户公司名称': name,
    '看板完成产量(万元)': round(bp, 2) if bp else None,  # 26年截至7月16日
    '25年完成产量(万元)': round(bp_25_full, 2) if bp_25_full else None,  # 全年
    '25年同期产量(万元)': round(bp_25_same, 2) if bp_25_same else None,  #同期
    ...
}

#同期同比增长率（使用同期产量计算）
prod26 = rec.get('看板完成产量(万元)')
prod25_same = rec.get('25年同期产量(万元)')
if prod26 and prod25_same and prod25_same > 0:
    rec['_同比增长率'] = (float(prod26) - float(prod25_same)) / float(prod25_same)
```

### 3. 国四客户数据

```python
guosi_data.append({
    'name': name,
    'prod26': r.get('看板完成产量(万元)'),
    'prod25': r.get('25年完成产量(万元)'),  # 全年（用于显示）
    'prod25_same': r.get('25年同期产量(万元)'),  #同期（用于计算全国同比）
    'yoy': r.get('_同比增长率'),
    ...
})
```

### 4. 全国同期同比计算

```python
# 计算全国同期同比（按产品，供参考）
national_yoy = {}
for prod in PRODUCTS:
    total_26 = sum(g.get('prod26', 0) or 0 for g in guosi_data if g.get('product_cap', {}).get(prod, 0) > 0)
    total_25_same = sum(g.get('prod25_same', 0) or 0 for g in guosi_data if g.get('product_cap', {}).get(prod, 0) > 0)
    if total_25_same > 0:
        national_yoy[prod] = (total_26 - total_25_same) / total_25_same
    else:
        national_yoy[prod] = None
```

**关键点**：全国同比必须使用 prod25_same（同期产量），不是 prod25（全年产量），否则会导致数值偏低。

### 5. 前端显示（template.html）

#### 表头
```javascript
h += '<th>' + lcProduct + '容量（万）</th><th>客户指标（万）</th><th>26年完成（万）</th><th>达成率</th><th>25年全年（万）</th><th>同期同比</th>';
```

#### 低于全国同比标红
```javascript
const yoyVal = item.yoy;
const natYoy = v.national_yoy && v.national_yoy[lcProduct];
const belowNat = natYoy !== null && natYoy !== undefined && yoyVal !== null && yoyVal !== undefined && yoyVal < natYoy;
const yoyCls = belowNat ? 'below-nat' : (yoyVal > 0 ? 'up' : yoyVal < 0 ? 'down' : 'zero');
h += '<td class="' + yoyCls + '">' + ... + '</td>';
```

#### CSS样式
```css
.below-nat { color: #a02020; font-weight: 700; background: #ffe0e0; }
```

#### 全国同比参考值显示
```javascript
function renderUpd() {
  const v = curView();
  document.getElementById('upd').textContent = '数据截止 ' + (v.updated || '-');

  // 全国同期同比参考值（仅标签一致性视图）
  const natYoyEl = document.getElementById('natYoy');
  if (v.view_type === 'label_consistency' && v.national_yoy && v.national_yoy[lcProduct] !== null && v.national_yoy[lcProduct] !== undefined) {
    const natYoy = v.national_yoy[lcProduct];
    const natYoyPct = (natYoy * 100).toFixed(1);
    const natYoySign = natYoy > 0 ? '+' : '';
    const natYoyColor = natYoy >= 0 ? '#1a7a3a' : '#a02020';
    natYoyEl.innerHTML = `全国${lcProduct}同比: <span style="color:${natYoyColor}">${natYoySign}${natYoyPct}%</span>`;
    natYoyEl.style.display = '';
  } else {
    natYoyEl.style.display = 'none';
  }
  ...
}
```

#### HTML结构
```html
<div class="infobar">
  <span class="nat-yoy" id="natYoy"></span>
  <span class="note" id="mainNote"></span>
  <span class="upd" id="upd"></span>
</div>
```

## 常见错误

### 错误1：使用全年产量计算同期同比
```python
# ❌ 错误
total_25 = sum(g.get('prod25', 0) or 0 for g in guosi_data ...)
national_yoy[prod] = (total_26 - total_25) / total_25
# 结果：欧洲只有0.3%（错误）

# ✅ 正确
total_25_same = sum(g.get('prod25_same', 0) or 0 for g in guosi_data ...)
national_yoy[prod] = (total_26 - total_25_same) / total_25_same
# 结果：欧洲37.5%（正确）
```

### 错误2：代码重复累加
```python
# ❌ 错误（第125行在if条件外又加了一次）
if order_date <= cutoff_date_2025 and dep_date.year == 2025:
    order_sum_2025[str(cc)] += float(amt) / 10000
order_sum_2025[str(cc)] += float(amt) / 10000  # 重复！

# ✅ 正确
if order_date <= cutoff_date_2025 and dep_date.year == 2025:
    order_sum_2025[str(cc)] += float(amt) / 10000
```

## 经验总结

**Why**: 同期同比必须使用同期的数据（截至相同日期），不能用全年数据，否则会低估或高估增长率。全国同比作为参考值，也必须使用同期数据计算。

**How to apply**:
1. 区分"全年产量"（用于显示）和"同期产量"（用于计算同比）
2. 全国同比计算必须使用 prod25_same，不是 prod25
3. 低于全国同比的客户标红，便于快速识别表现不佳的客户
4. 表头明确标注"25年全年"和"同期同比"，避免混淆

## 参考数据

国四客户全国同期同比（示例）：
- 欧洲：37.5%
- 美洲：81.6%
- 澳新：49.3%
- 中东非：37.6%
- 中亚高加索：92.9%
