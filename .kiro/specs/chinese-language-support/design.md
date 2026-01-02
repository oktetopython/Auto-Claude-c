# Design Document: Chinese Language Support

## Overview

本设计文档描述如何为Kangaroo项目的GUI界面添加简体中文语言支持。项目已有基于react-i18next的国际化框架，目前支持英语(en)和法语(fr)。本设计将扩展该框架以支持简体中文(zh)。

## Architecture

### 现有国际化架构

```
apps/frontend/src/
├── shared/
│   ├── constants/
│   │   └── i18n.ts              # 语言类型定义和可用语言列表
│   └── i18n/
│       ├── index.ts             # i18n初始化配置
│       └── locales/
│           ├── en/              # 英文翻译文件
│           │   ├── common.json
│           │   ├── navigation.json
│           │   ├── settings.json
│           │   ├── tasks.json
│           │   ├── welcome.json
│           │   ├── onboarding.json
│           │   ├── dialogs.json
│           │   ├── gitlab.json
│           │   └── taskReview.json
│           └── fr/              # 法文翻译文件
│               └── (同上结构)
└── renderer/
    ├── components/settings/
    │   └── LanguageSettings.tsx # 语言选择组件
    └── stores/
        └── settings-store.ts    # 设置状态管理
```

### 扩展后的架构

```
apps/frontend/src/shared/i18n/locales/
├── en/                          # 英文翻译 (现有)
├── fr/                          # 法文翻译 (现有)
└── zh/                          # 中文翻译 (新增)
    ├── common.json
    ├── navigation.json
    ├── settings.json
    ├── tasks.json
    ├── welcome.json
    ├── onboarding.json
    ├── dialogs.json
    ├── gitlab.json
    └── taskReview.json
```

## Components and Interfaces

### 1. 语言类型定义 (i18n.ts)

```typescript
// apps/frontend/src/shared/constants/i18n.ts

export type SupportedLanguage = 'en' | 'fr' | 'zh';

export const AVAILABLE_LANGUAGES = [
  { value: 'en' as const, label: 'English', nativeLabel: 'English' },
  { value: 'fr' as const, label: 'French', nativeLabel: 'Français' },
  { value: 'zh' as const, label: 'Chinese', nativeLabel: '简体中文' }
] as const;

export const DEFAULT_LANGUAGE: SupportedLanguage = 'en';
```

### 2. i18n初始化配置 (index.ts)

```typescript
// apps/frontend/src/shared/i18n/index.ts

// Import Chinese translation resources (新增)
import zhCommon from './locales/zh/common.json';
import zhNavigation from './locales/zh/navigation.json';
import zhSettings from './locales/zh/settings.json';
import zhTasks from './locales/zh/tasks.json';
import zhWelcome from './locales/zh/welcome.json';
import zhOnboarding from './locales/zh/onboarding.json';
import zhDialogs from './locales/zh/dialogs.json';
import zhGitlab from './locales/zh/gitlab.json';
import zhTaskReview from './locales/zh/taskReview.json';

export const resources = {
  en: { /* existing */ },
  fr: { /* existing */ },
  zh: {
    common: zhCommon,
    navigation: zhNavigation,
    settings: zhSettings,
    tasks: zhTasks,
    welcome: zhWelcome,
    onboarding: zhOnboarding,
    dialogs: zhDialogs,
    gitlab: zhGitlab,
    taskReview: zhTaskReview
  }
} as const;
```

### 3. 语言选择组件 (LanguageSettings.tsx)

现有组件已支持动态渲染AVAILABLE_LANGUAGES数组，无需修改组件代码。添加中文到AVAILABLE_LANGUAGES后，组件将自动显示中文选项。

## Data Models

### 翻译资源文件结构

每个翻译文件遵循相同的JSON结构，键名与英文版本完全一致：

```json
{
  "key": "翻译文本",
  "nested": {
    "key": "嵌套翻译文本"
  },
  "withPlaceholder": "包含 {{count}} 个项目",
  "plural": "{{count}} 个项目",
  "plural_plural": "{{count}} 个项目"
}
```

### 翻译命名空间

| 命名空间 | 用途 | 预估键数量 |
|---------|------|-----------|
| common | 通用文本、按钮、标签 | ~150 |
| navigation | 导航菜单项 | ~30 |
| settings | 设置界面 | ~200 |
| tasks | 任务相关 | ~60 |
| welcome | 欢迎页面 | ~15 |
| onboarding | 引导向导 | ~80 |
| dialogs | 对话框 | ~100 |
| gitlab | GitLab集成 | ~120 |
| taskReview | 任务审查 | ~5 |

## Correctness Properties

*A property is a characteristic or behavior that should hold true across all valid executions of a system-essentially, a formal statement about what the system should do. Properties serve as the bridge between human-readable specifications and machine-verifiable correctness guarantees.*

### Property 1: Translation Key Completeness

*For any* translation key that exists in the English resource files, there SHALL be a corresponding key with the same path in the Chinese resource files.

**Validates: Requirements 2.1-2.9, 5.1**

### Property 2: Placeholder Preservation

*For any* translation string in English that contains placeholders (matching pattern `{{[^}]+}}`), the corresponding Chinese translation SHALL contain exactly the same placeholders.

**Validates: Requirements 5.4**

### Property 3: Plural Form Completeness

*For any* translation key in English that has plural variants (keys ending with `_plural`), the Chinese translation SHALL have corresponding plural variant keys.

**Validates: Requirements 5.5**

### Property 4: Simplified Chinese Character Validation

*For any* Chinese translation string, all Chinese characters SHALL be valid simplified Chinese characters (within Unicode ranges for CJK Unified Ideographs commonly used in simplified Chinese).

**Validates: Requirements 5.2**

## Error Handling

### 翻译缺失处理

i18next框架已配置fallbackLng为'en'，当中文翻译缺失时：
1. 系统自动回退到英文翻译
2. 开发环境下在控制台输出警告
3. 用户界面不会显示空白或键名

### 语言切换错误处理

```typescript
const handleLanguageChange = async (newLanguage: SupportedLanguage) => {
  try {
    await i18n.changeLanguage(newLanguage);
    updateStoreSettings({ language: newLanguage });
  } catch (error) {
    console.error('Failed to change language:', error);
    // 保持当前语言不变
  }
};
```

## Testing Strategy

### 单元测试

1. **类型定义测试**: 验证SupportedLanguage类型包含'zh'
2. **语言列表测试**: 验证AVAILABLE_LANGUAGES包含中文条目
3. **资源注册测试**: 验证resources对象包含'zh'键和所有命名空间

### 属性测试 (Property-Based Testing)

使用fast-check库进行属性测试：

1. **翻译键完整性测试**: 遍历所有英文键，验证中文翻译存在
2. **占位符保留测试**: 提取英文占位符，验证中文翻译包含相同占位符
3. **复数形式测试**: 检查英文复数键，验证中文对应键存在
4. **字符验证测试**: 验证中文翻译使用简体中文字符

### 集成测试

1. **语言切换测试**: 模拟用户切换到中文，验证界面更新
2. **持久化测试**: 验证语言设置保存和加载
3. **组件渲染测试**: 验证LanguageSettings组件显示中文选项

### 测试配置

- 属性测试最少运行100次迭代
- 每个属性测试标注对应的设计属性编号
- 标签格式: **Feature: chinese-language-support, Property N: {property_text}**
