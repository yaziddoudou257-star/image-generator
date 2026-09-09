#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
مثال متقدم - توليد صور مشابهة للصور المرفقة
Advanced example - Generate images similar to uploaded photos
"""

from generate_image import ImageGenerator

# إنشاء مولد الصور
generator = ImageGenerator()

# قائمة الأوصاف المتعددة
prompts = [
    # وصف الصورة الأولى (سيلفي في السيارة)
    "selfie of a couple sitting inside a car, woman wearing blue hijab and blue dress, man wearing dark blue shirt and black cap, natural lighting, high quality photo",
    
    # وصف الصورة الثانية (بجانب النهر)
    "couple taking selfie by the river, woman in blue hijab and blue dress eating ice cream, man in black striped shirt, ancient stone bridge in background, sunny day, food on table, coca cola, professional photo",
    
    # وصف إضافي - سيلفي عام
    "beautiful selfie portrait of a couple, smiling, natural daylight, professional photography",
]

print("=" * 60)
print("🎨 مولد الصور - أمثلة متقدمة")
print("=" * 60)

# توليد صورة لكل وصف
for i, prompt in enumerate(prompts, 1):
    print(f"\n📸 الصورة #{i}")
    print(f"الوصف: {prompt}\n")
    
    # توليد الصورة
    images = generator.generate(
        prompt=prompt,
        num_images=1,
        steps=50,  # يمكن زيادته لجودة أفضل (75)
        guidance_scale=7.5
    )
    
    # حفظ الصورة
    generator.save_images(images)
    print("-" * 60)

print("\n✨ تم الانتهاء! جميع الصور محفوظة في مجلد 'generated_images'")
