# Material Design设计规范整理

内容来自[https://material.google.com/](https://material.google.com/)。

※ 'Material' 在这里翻译为“元素”以便与“组件”中的“卡片”区别。

## 形而上

### [环境](https://material.google.com/material-design/environment.html)

- 任何元素都只有**1 dp**的厚度。
- 阴影由元素在z轴上的高度自然形成。

### [元素固有属性](https://material.google.com/material-design/material-properties.html)

#### 元素的物理属性

- 任何元素都只有**1 dp**的厚度；**没有例外**。
- 阴影由元素在z轴上的高度自然形成；不是强行画出来的。
- 元素上的内容不增加元素的厚度。
- 元素中的内容可以独立于元素，可以在元素中自由变化，但是内容不能超出元素边界。
- 用户输入、事件不能穿越元素导致多个元素响应。
- 多个元素不可以在同一个z值的平面相重合交叉。
- 元素不能在升降的时候穿越其他元素。

#### 元素的动态属性

- 元素可以改变形状；可以自由变换成矩形或圆形。
- 元素只在它所在的平面上伸缩。
- 元素不可以翻折、折角。
- 多个元素可以聚合成一个元素；单个元素可以拆分成多个元素。

#### 元素的运动

- 元素可以在环境中自然产生、消失。
- 元素可以沿任意坐标轴移动。
- 元素的z值（高度值）通常是由于用户与元素的交互产生的。

### [升降和阴影](https://material.google.com/material-design/elevation-shadows.html)



#### 

## 布局

### 单位和度量

- 