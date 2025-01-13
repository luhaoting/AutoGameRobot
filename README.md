- Ultralytics YOLO: Official implementation of YOLO for object detection.
- Gym: For defining and simulating game environments.
- PyAutoGUI: For simulating mouse and keyboard operations.

+ install 
`pip install -r requirements.txt`

#### Project Directory Structure
- **`game_automation/`**: The root directory of the project.
  - **`data/`**: Contains data used for training and testing.
    - **`images/`**: Stores game screenshots.
    - **`labels/`**: Stores annotation files for the images.
  - **`models/`**: Contains pre-trained and trained models.
    - **`yolov8n.pt`**: Pre-trained YOLO model.
    - **`dqn_model.pth`**: Trained DQN model.
  - **`scripts/`**: Contains Python scripts for training and running the project.
    - **`train_yolo.py`**: Script to train the YOLO model.
    - **`train_dqn.py`**: Script to train the DQN model.
    - **`play_game.py`**: Script to run game automation.
  - **`utils/`**: Contains utility functions and modules.
    - **`yolo_utils.py`**: Utility functions for YOLO.
    - **`dqn_utils.py`**: Utility functions for DQN.
  - **`requirements.txt`**: Lists all project dependencies.
  - **`README.md`**: Project documentation and setup instructions.