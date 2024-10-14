
# 提取影片字幕的Python腳本

此Python腳本用於從指定的影片中提取字幕並保存為 `.srt` 格式文件，方便您進一步處理或編輯字幕。

## 功能概述

- 使用 **ffmpeg** 從影片文件中提取字幕。
- 支援 `.MP4` 格式影片，並將字幕保存為 `.srt` 文件。
- 處理過程包括錯誤處理，以確保 ffmpeg 存在並檢查影片文件是否存在。

## 先決條件

### 系統要求
- **Python 版本**：Python 3.x
- **ffmpeg**：確保您的系統已安裝 `ffmpeg` 並且在 PATH 中可用。

### Python 庫
- 標準庫：`os` 和 `subprocess`（無需額外安裝）

## 安裝指南

### 1. 安裝 ffmpeg

根據您的系統選擇適合的安裝方式：

- **Ubuntu/Debian**：
  ```bash
  sudo apt update
  sudo apt install ffmpeg
  ```

- **Windows**：
  下載 [ffmpeg](https://ffmpeg.org/download.html)，將其添加到系統的 PATH 中。

- **Mac**：
  使用 Homebrew 安裝：
  ```bash
  brew install ffmpeg
  ```

### 2. 克隆或下載腳本

```bash
git clone https://your-repo-url.git
cd your-repo-url
```

## 使用方法

1. **準備影片文件**：

   - 將影片文件（如 `DJI_0132.MP4`）存放在對應的路徑下：  
     `/home/ubuntu/大疆影片/0132/`

2. **執行腳本**：

   在終端中運行以下命令：

   ```bash
   python your_script_name.py
   ```

   **注意**：請將 `your_script_name.py` 替換為實際的腳本文件名。

3. **查看輸出結果**：

   如果成功提取，字幕將保存為 `/home/ubuntu/大疆影片/0132/DJI_0132srt`。

## 腳本邏輯

1. **檢查影片是否存在**：
   - 使用 `os.path.exists()` 確認影片路徑是否正確。

2. **執行字幕提取**：
   - 使用 `subprocess.run()` 調用 ffmpeg 提取字幕，並將其保存為 `.srt` 文件。

3. **錯誤處理**：
   - 如果 ffmpeg 無法找到或影片文件不存在，將輸出相應的錯誤訊息。

## 常見問題

### 1. 運行時出現 `ffmpeg: not found` 錯誤
- 請檢查 ffmpeg 是否已安裝並在 PATH 中。

### 2. 提取後沒有字幕文件
- 確認影片文件包含字幕軌，並確保軌道索引（如 `0:s:0`）正確。

### 3. 找不到影片文件
- 請檢查影片路徑是否正確，以及文件是否存在。

## 版本資訊

- **版本**：1.0.0
- **日期**：2024 年 10 月 14 日
- **作者**：您的姓名

## 聯繫方式

如果您有任何問題或建議，請聯繫：

- **電子郵件**：your.email@example.com
- **GitHub**：https://github.com/your-github-profile

## 授權

此腳本基於 MIT 授權條款發布。詳情請參閱 [LICENSE](LICENSE) 文件。

---

**感謝您使用此腳本！希望它能幫助您輕鬆提取影片字幕。**
