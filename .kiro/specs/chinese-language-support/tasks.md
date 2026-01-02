# Implementation Plan: Chinese Language Support

## Overview

本实现计划将为Kangaroo项目GUI界面添加简体中文语言支持。实现将按照以下顺序进行：类型定义更新 → 翻译文件创建 → i18n配置更新 → 测试验证。

## Tasks

- [x] 1. Update language type definitions and constants
  - [x] 1.1 Add 'zh' to SupportedLanguage type in i18n.ts
    - Modify `apps/frontend/src/shared/constants/i18n.ts`
    - Add 'zh' to the SupportedLanguage union type
    - Add Chinese entry to AVAILABLE_LANGUAGES array with value 'zh', label 'Chinese', nativeLabel '简体中文'
    - _Requirements: 1.1, 1.2, 1.3_

- [x] 2. Create Chinese translation resource files
  - [x] 2.1 Create zh/common.json translation file
    - Create `apps/frontend/src/shared/i18n/locales/zh/common.json`
    - Translate all keys from en/common.json to simplified Chinese
    - Preserve all placeholder syntax ({{count}}, etc.)
    - _Requirements: 2.1, 5.1, 5.4_

  - [x] 2.2 Create zh/navigation.json translation file
    - Create `apps/frontend/src/shared/i18n/locales/zh/navigation.json`
    - Translate all keys from en/navigation.json to simplified Chinese
    - _Requirements: 2.2, 5.1_

  - [x] 2.3 Create zh/settings.json translation file
    - Create `apps/frontend/src/shared/i18n/locales/zh/settings.json`
    - Translate all keys from en/settings.json to simplified Chinese
    - _Requirements: 2.3, 5.1_

  - [x] 2.4 Create zh/tasks.json translation file
    - Create `apps/frontend/src/shared/i18n/locales/zh/tasks.json`
    - Translate all keys from en/tasks.json to simplified Chinese
    - _Requirements: 2.4, 5.1_

  - [x] 2.5 Create zh/welcome.json translation file
    - Create `apps/frontend/src/shared/i18n/locales/zh/welcome.json`
    - Translate all keys from en/welcome.json to simplified Chinese
    - _Requirements: 2.5, 5.1_

  - [x] 2.6 Create zh/onboarding.json translation file
    - Create `apps/frontend/src/shared/i18n/locales/zh/onboarding.json`
    - Translate all keys from en/onboarding.json to simplified Chinese
    - _Requirements: 2.6, 5.1_

  - [x] 2.7 Create zh/dialogs.json translation file
    - Create `apps/frontend/src/shared/i18n/locales/zh/dialogs.json`
    - Translate all keys from en/dialogs.json to simplified Chinese
    - _Requirements: 2.7, 5.1_

  - [x] 2.8 Create zh/gitlab.json translation file
    - Create `apps/frontend/src/shared/i18n/locales/zh/gitlab.json`
    - Translate all keys from en/gitlab.json to simplified Chinese
    - _Requirements: 2.8, 5.1_

  - [x] 2.9 Create zh/taskReview.json translation file
    - Create `apps/frontend/src/shared/i18n/locales/zh/taskReview.json`
    - Translate all keys from en/taskReview.json to simplified Chinese
    - _Requirements: 2.9, 5.1_

- [x] 3. Register Chinese translations in i18n system
  - [x] 3.1 Update i18n index.ts to import and register Chinese translations
    - Modify `apps/frontend/src/shared/i18n/index.ts`
    - Add import statements for all Chinese translation files
    - Add 'zh' entry to resources object with all namespaces
    - _Requirements: 3.1, 3.2, 3.3_

- [x] 4. Checkpoint - Verify basic functionality
  - Ensure TypeScript compiles without errors
  - Verify all translation files are valid JSON
  - Ask the user if questions arise

- [ ]* 5. Write property tests for translation completeness
  - [ ]* 5.1 Write property test for translation key completeness
    - **Property 1: Translation Key Completeness**
    - **Validates: Requirements 2.1-2.9, 5.1**
    - Create test file `apps/frontend/src/__tests__/i18n-chinese.test.ts`
    - For all keys in English translations, verify corresponding Chinese key exists

  - [ ]* 5.2 Write property test for placeholder preservation
    - **Property 2: Placeholder Preservation**
    - **Validates: Requirements 5.4**
    - For all English strings with placeholders, verify Chinese has same placeholders

  - [ ]* 5.3 Write property test for plural form completeness
    - **Property 3: Plural Form Completeness**
    - **Validates: Requirements 5.5**
    - For all English plural keys, verify Chinese has corresponding plural keys

- [ ]* 6. Write unit tests for language configuration
  - [ ]* 6.1 Write unit tests for language type and constants
    - Test SupportedLanguage includes 'zh'
    - Test AVAILABLE_LANGUAGES contains Chinese entry with correct values
    - Test backward compatibility with 'en' and 'fr'
    - _Requirements: 1.1, 1.2, 1.3_

  - [ ]* 6.2 Write unit tests for i18n resource registration
    - Test resources object contains 'zh' key
    - Test all namespaces are registered under 'zh'
    - _Requirements: 3.1, 3.2_

- [x] 7. Final checkpoint - Ensure all tests pass
  - Run all property tests and unit tests
  - Verify no TypeScript errors
  - Ask the user if questions arise

- [x] 8. Update page components to use translations
  - [x] 8.1 Create pages.json translation files
    - Created `apps/frontend/src/shared/i18n/locales/en/pages.json`
    - Created `apps/frontend/src/shared/i18n/locales/zh/pages.json`
    - Added translations for Roadmap, Ideation, Changelog, Worktrees, etc.
    - Registered pages namespace in i18n configuration

  - [x] 8.2 Update Worktrees component
    - Updated `apps/frontend/src/renderer/components/Worktrees.tsx`
    - Replaced all hardcoded strings with i18n translations
    - Added translations for merge dialog, delete dialog, stats

  - [x] 8.3 Update Changelog components
    - Updated `apps/frontend/src/renderer/components/changelog/Changelog.tsx`
    - Updated `apps/frontend/src/renderer/components/changelog/ChangelogHeader.tsx`
    - Updated `apps/frontend/src/renderer/components/changelog/ChangelogList.tsx`
    - Updated `apps/frontend/src/renderer/components/changelog/ChangelogFilters.tsx`
    - Replaced hardcoded strings with i18n translations

  - [x] 8.4 Update Roadmap components (previously completed)
    - Updated RoadmapEmptyState.tsx
    - Updated RoadmapHeader.tsx

  - [x] 8.5 Update Ideation components (previously completed)
    - Updated IdeationEmptyState.tsx

- [x] 9. Comprehensive translation audit - Fix remaining hardcoded strings
  - [x] 9.1 Update TaskDetailModal.tsx with translations
    - Added `detail` section to tasks.json for both en and zh locales
    - Replaced hardcoded strings: "Recovering...", "Recover Task", "Resume Task", "Start Task", "Stop Task", "Task completed", "Delete Task", "Close"
    - Replaced tab names: "Overview", "Subtasks", "Logs"
    - Replaced delete confirmation dialog strings
    - _Requirements: 2.4, 5.1_

  - [x] 9.2 Update AddWorkspaceModal.tsx with translations
    - Added `workspace` section to pages.json for both en and zh locales
    - Replaced hardcoded strings: "Create Workspace", "Cancel", "Creating...", form labels, placeholders
    - _Requirements: 5.1_

  - [x] 9.3 Update ChatHistorySidebar.tsx with translations
    - Added `chatHistory` section to pages.json for both en and zh locales
    - Replaced hardcoded strings: "Chat History", "No conversations yet", "Today", "Yesterday", "days ago", "Delete conversation?", "Cancel", "Delete", "Rename"
    - _Requirements: 5.1_

  - [x] 9.4 Update other components with hardcoded strings
    - TaskActions.tsx - Added useTranslation, replaced all hardcoded strings
    - DiscardDialog.tsx - Added useTranslation, replaced all hardcoded strings
    - DiffViewDialog.tsx - Added useTranslation, replaced all hardcoded strings
    - ConflictDetailsDialog.tsx - Added useTranslation, replaced all hardcoded strings
    - _Requirements: 5.1_

## Notes

- Tasks marked with `*` are optional and can be skipped for faster MVP
- Each task references specific requirements for traceability
- Checkpoints ensure incremental validation
- Property tests validate universal correctness properties
- Translation files should use consistent terminology throughout
