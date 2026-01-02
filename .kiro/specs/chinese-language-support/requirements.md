# Requirements Document

## Introduction

本功能为Kangaroo项目的GUI界面添加简体中文语言支持，使用户可以在英语和中文之间切换界面语言。项目已有完善的国际化框架（react-i18next），目前支持英语和法语，本功能将在此基础上扩展中文支持。

## Glossary

- **i18n_System**: 国际化系统，基于react-i18next实现的多语言支持框架
- **Translation_Resource**: 翻译资源文件，JSON格式的键值对文件，存储特定语言的翻译文本
- **Language_Selector**: 语言选择器组件，允许用户在设置界面选择界面语言
- **Supported_Language**: 支持的语言类型定义，TypeScript类型约束

## Requirements

### Requirement 1: Add Chinese Language Type Definition

**User Story:** As a developer, I want the Chinese language type to be defined in the i18n constants, so that TypeScript can properly validate Chinese language usage throughout the codebase.

#### Acceptance Criteria

1. WHEN the i18n constants file is loaded, THE i18n_System SHALL include 'zh' as a valid SupportedLanguage type
2. WHEN the AVAILABLE_LANGUAGES array is accessed, THE i18n_System SHALL include a Chinese language entry with value 'zh', label 'Chinese', and nativeLabel '简体中文'
3. THE i18n_System SHALL maintain backward compatibility with existing 'en' and 'fr' language definitions

### Requirement 2: Create Chinese Translation Resource Files

**User Story:** As a user, I want all interface text to be available in Chinese, so that I can use the application entirely in my native language.

#### Acceptance Criteria

1. WHEN the application loads Chinese translations, THE i18n_System SHALL provide a complete zh/common.json file with all keys matching en/common.json
2. WHEN the application loads Chinese translations, THE i18n_System SHALL provide a complete zh/navigation.json file with all keys matching en/navigation.json
3. WHEN the application loads Chinese translations, THE i18n_System SHALL provide a complete zh/settings.json file with all keys matching en/settings.json
4. WHEN the application loads Chinese translations, THE i18n_System SHALL provide a complete zh/tasks.json file with all keys matching en/tasks.json
5. WHEN the application loads Chinese translations, THE i18n_System SHALL provide a complete zh/welcome.json file with all keys matching en/welcome.json
6. WHEN the application loads Chinese translations, THE i18n_System SHALL provide a complete zh/onboarding.json file with all keys matching en/onboarding.json
7. WHEN the application loads Chinese translations, THE i18n_System SHALL provide a complete zh/dialogs.json file with all keys matching en/dialogs.json
8. WHEN the application loads Chinese translations, THE i18n_System SHALL provide a complete zh/gitlab.json file with all keys matching en/gitlab.json
9. WHEN the application loads Chinese translations, THE i18n_System SHALL provide a complete zh/taskReview.json file with all keys matching en/taskReview.json

### Requirement 3: Register Chinese Translations in i18n System

**User Story:** As a developer, I want Chinese translations to be properly registered in the i18n initialization, so that the application can load and use Chinese translations at runtime.

#### Acceptance Criteria

1. WHEN the i18n system initializes, THE i18n_System SHALL import all Chinese translation resource files
2. WHEN the i18n system initializes, THE i18n_System SHALL register Chinese translations in the resources object under the 'zh' key
3. WHEN a user selects Chinese language, THE i18n_System SHALL successfully load and apply all Chinese translations

### Requirement 4: Enable Chinese Language Selection in UI

**User Story:** As a user, I want to see Chinese as an option in the language settings, so that I can switch the interface to Chinese.

#### Acceptance Criteria

1. WHEN a user opens the Language Settings section, THE Language_Selector SHALL display Chinese (简体中文) as a selectable option
2. WHEN a user clicks on the Chinese language option, THE Language_Selector SHALL immediately apply Chinese translations to the interface
3. WHEN a user saves settings after selecting Chinese, THE i18n_System SHALL persist the language preference
4. WHEN the application restarts with Chinese as the saved language, THE i18n_System SHALL load the interface in Chinese

### Requirement 5: Ensure Translation Completeness and Quality

**User Story:** As a user, I want all Chinese translations to be accurate and complete, so that I can fully understand and use all application features.

#### Acceptance Criteria

1. FOR ALL translation keys in English resource files, THE Translation_Resource SHALL have corresponding Chinese translations
2. THE Translation_Resource SHALL use proper simplified Chinese characters (简体中文)
3. THE Translation_Resource SHALL maintain consistent terminology throughout all translation files
4. WHEN a translation contains placeholders (e.g., {{count}}), THE Translation_Resource SHALL preserve the placeholder syntax exactly
5. WHEN a translation has plural forms, THE Translation_Resource SHALL provide appropriate Chinese translations for all plural variants
