# Visual Usability Checker Automation Artifact

This minimal automation script checks the visual usability of a web page by capturing a screenshot and running a basic contrast ratio analysis.

```python
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image
import numpy as np

def capture_screenshot(url, output_path='screenshot.png'):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1920, 1080)
    driver.get(url)
    driver.save_screenshot(output_path)
    driver.quit()
    return output_path

def average_luminance(image_path):
    img = Image.open(image_path).convert('RGB')
    arr = np.array(img)
    # Relative luminance formula
    lum = 0.2126*arr[...,0] + 0.7152*arr[...,1] + 0.0722*arr[...,2]
    return lum.mean() / 255

def contrast_ratio(lum1, lum2):
    L1, L2 = max(lum1, lum2), min(lum1, lum2)
    return (L1 + 0.05) / (L2 + 0.05)

if __name__ == '__main__':
    url = sys.argv[1] if len(sys.argv) > 1 else 'https://example.com'
    screenshot = capture_screenshot(url)
    lum = average_luminance(screenshot)
    # Assume white background for comparison
    contrast = contrast_ratio(lum, 1.0)
    print(f'Average luminance: {lum:.3f}')
    print(f'Contrast ratio against white: {contrast:.2f}')
    if contrast < 4.5:
        print('⚠️ Low contrast – may fail WCAG AA criteria')
    else:
        print('✅ Contrast OK')
```

*Save this script as `visual_usability_check.py` and run it with the target URL.*
