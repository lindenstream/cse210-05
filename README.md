# cse210-05
Week 09 Cycle Game

Game Specification: https://byui-cse.github.io/cse210-course-competency/polymorphism/materials/cycle-specification.html

Group Members:
- Brock Ford
- Ashlee Butterfield
- Spencer Christensen
- Zachary Lindstrom
- Sayri Quinchiguango

Overview
Cycle is a game where the players try to cut each other off using cycles that leave a trail behind them.

Rules
Cycle is played according to the following rules.
- Players can move up, down, left and right...
    - Player one moves using the W, S, A and D keys.
    - Player two moves using the I, K, J and L keys.
- Each player's trail grows as they move.
- Players try to maneuver so the opponent collides with their trail.
- If a player collides with their opponent's trail...
    - A "game over" message is displayed in the middle of the screen.
    - The cycles turn white.
    - Players keep moving and turning but don't run into each other.

Requirements
The program must also meet the following requirements.
- The program must include a README file.
- The program must include class and method comments.
- The program must have at least 16 classes.
- The program must remain true to game play described in the overview.

Have Some Fun
Have some fun by enhancing the game any way you like. A few ideas are as follows.
- Enhanced scoring and game reset.
- Enhanced game play and game over messages.
- Enhanced game display, e.g. cycle and trails

List of Classes:
- (1) Actor
- (2) Cast
- (3) Cycle
- (4) Cycle1
- (5) Score
- (6) Director
- (7) Action
- (8) control_actors_action
- (9) draw_actors_action
- (10) handle_collisions_action
- (11) move_actors_action
- (12) keyboard_service
- (13) video_service
- (14) Color
- (15) Point
- (16) Cycle2