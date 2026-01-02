---
description: "Task list template for feature implementation"
---

# Tasks: Console Todo App

**Input**: Design documents from `/specs/1-console-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project structure per implementation plan
- [x] T002 [P] Create directory structure: src/models/, src/services/, src/cli/, src/lib/, tests/unit/, tests/integration/, tests/contract/
- [x] T003 [P] Create basic __init__.py files in all directories

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

Examples of foundational tasks (adjust based on your project):

- [x] T004 Create TodoItem model in src/models/todo_item.py
- [x] T005 Create TodoManager service in src/services/todo_manager.py (foundational structure only)
- [x] T006 [P] Create main CLI application in src/cli/main.py (basic structure only)
- [x] T007 Setup in-memory storage structure in TodoManager
- [x] T008 Create utility functions for ID generation in src/lib/utils.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add New Todo (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new tasks to their todo list so they can keep track of work that needs to be done

**Independent Test**: Can be fully tested by running the command with a task description and verifying the task appears in the list.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T009 [P] [US1] Contract test for add command in tests/contract/test_todo_contracts.py
- [ ] T010 [P] [US1] Unit test for TodoItem creation in tests/unit/models/test_todo_item.py
- [ ] T011 [P] [US1] Unit test for TodoManager add functionality in tests/unit/services/test_todo_manager.py

### Implementation for User Story 1

- [x] T012 [P] [US1] Implement TodoItem model with id, description, completed attributes in src/models/todo_item.py
- [x] T013 [P] [US1] Implement TodoManager.add() method in src/services/todo_manager.py
- [x] T014 [US1] Implement add command handler in src/cli/main.py
- [x] T015 [US1] Add validation for description (not empty/whitespace) in src/services/todo_manager.py
- [x] T016 [US1] Add unique ID assignment logic in src/services/todo_manager.py
- [x] T017 [US1] Add success/error message handling for add operation in src/cli/main.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View Todo List (Priority: P1)

**Goal**: Allow users to see all their pending tasks so they can prioritize their work

**Independent Test**: Can be fully tested by adding tasks and then viewing the complete list to verify all tasks are displayed correctly.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [ ] T018 [P] [US2] Contract test for list/view command in tests/contract/test_todo_contracts.py
- [ ] T019 [P] [US2] Unit test for TodoManager list functionality in tests/unit/services/test_todo_manager.py

### Implementation for User Story 2

- [x] T020 [P] [US2] Implement TodoManager.list() method in src/services/todo_manager.py
- [x] T021 [US2] Implement list/view command handler in src/cli/main.py
- [x] T022 [US2] Add formatted display of todos with ID, description, and completion status in src/cli/main.py
- [x] T023 [US2] Add handling for empty todo list case in src/cli/main.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Mark Todo Complete (Priority: P2)

**Goal**: Allow users to mark tasks as complete so they can track their progress and focus on remaining work

**Independent Test**: Can be tested by marking a task complete and then viewing the list to verify the status has changed.

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [ ] T024 [P] [US3] Contract test for complete command in tests/contract/test_todo_contracts.py
- [ ] T025 [P] [US3] Unit test for TodoManager complete functionality in tests/unit/services/test_todo_manager.py

### Implementation for User Story 3

- [x] T026 [P] [US3] Implement TodoManager.mark_complete() method in src/services/todo_manager.py
- [x] T027 [US3] Implement complete command handler in src/cli/main.py
- [x] T028 [US3] Add validation for valid todo ID in src/services/todo_manager.py
- [x] T029 [US3] Add success/error message handling for complete operation in src/cli/main.py

**Checkpoint**: User Stories 1, 2, AND 3 should now be independently functional

---

## Phase 6: User Story 4 - Update Todo Description (Priority: P3)

**Goal**: Allow users to modify the description of a task if their understanding of the work changes

**Independent Test**: Can be tested by updating a task description and then viewing the task to verify the description has changed.

### Tests for User Story 4 (OPTIONAL - only if tests requested) ⚠️

- [ ] T030 [P] [US4] Contract test for update command in tests/contract/test_todo_contracts.py
- [ ] T031 [P] [US4] Unit test for TodoManager update functionality in tests/unit/services/test_todo_manager.py

### Implementation for User Story 4

- [x] T032 [P] [US4] Implement TodoManager.update() method in src/services/todo_manager.py
- [x] T033 [US4] Implement update command handler in src/cli/main.py
- [x] T034 [US4] Add validation for valid todo ID and non-empty description in src/services/todo_manager.py
- [x] T035 [US4] Add success/error message handling for update operation in src/cli/main.py

**Checkpoint**: User Stories 1, 2, 3, AND 4 should now be independently functional

---

## Phase 7: User Story 5 - Delete Todo (Priority: P3)

**Goal**: Allow users to remove tasks that are no longer relevant to keep their todo list focused and manageable

**Independent Test**: Can be tested by deleting a task and then viewing the list to verify the task is no longer present.

### Tests for User Story 5 (OPTIONAL - only if tests requested) ⚠️

- [ ] T036 [P] [US5] Contract test for delete command in tests/contract/test_todo_contracts.py
- [ ] T037 [P] [US5] Unit test for TodoManager delete functionality in tests/unit/services/test_todo_manager.py

### Implementation for User Story 5

- [x] T038 [P] [US5] Implement TodoManager.delete() method in src/services/todo_manager.py
- [x] T039 [US5] Implement delete command handler in src/cli/main.py
- [x] T040 [US5] Add validation for valid todo ID in src/services/todo_manager.py
- [x] T041 [US5] Add success/error message handling for delete operation in src/cli/main.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T042 [P] Documentation updates in README.md and docs/
- [x] T043 Code cleanup and refactoring across all modules
- [x] T044 [P] Add error handling for invalid commands in src/cli/main.py
- [x] T045 [P] Add command-line argument parsing using argparse in src/cli/main.py
- [x] T046 [P] Add integration tests in tests/integration/test_cli_integration.py
- [x] T047 Run quickstart.md validation

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 4 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 5 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
Task: "Contract test for add command in tests/contract/test_todo_contracts.py"
Task: "Unit test for TodoItem creation in tests/unit/models/test_todo_item.py"
Task: "Unit test for TodoManager add functionality in tests/unit/services/test_todo_manager.py"

# Launch all models for User Story 1 together:
Task: "Implement TodoItem model with id, description, completed attributes in src/models/todo_item.py"
Task: "Implement TodoManager.add() method in src/services/todo_manager.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence