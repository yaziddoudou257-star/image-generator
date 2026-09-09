#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
أداة تفاعلية لتوليد الصور
Interactive tool to generate images
"""

from generate_image import ImageGenerator

def interactive_mode():
    """وضع تفاعلي لتوليد الصور"""
    
    # إنشاء المولد
    generator = ImageGenerator()
    
    print("\n" + "=" * 70)
    print("🎨 مولد الصور التفاعلي")
    print("=" * 70)
    print("\n💡 نصائح:")
    print("   - اكتب وصفاً تفصيلياً للصورة التي تريدها")
    print("   - يمكنك الكتابة بالعربية أو الإنجليزية")
    print("   - اكتب 'exit' للخروج\n")
    
    while True:
        # إدخال الوصف
        prompt = input("📝 ادخل وصف الصورة: ").strip()
        
        if prompt.lower() == 'exit':
            print("\n👋 شكراً لاستخدام مولد الصور!")
            break
        
        if not prompt:
            print("❌ الرجاء إدخال وصف!\n")
            continue
        
        # إدخال الخيارات الإضافية
        try:
            num = input("🖼️  عدد الصور (افتراضي: 1): ").strip()
            num_images = int(num) if num else 1
            
            steps = input("⚙️  عدد الخطوات (افتراضي: 30، أقصى: 75): ").strip()
            steps = int(steps) if steps else 30
            steps = min(steps, 75)  # حد أقصى 75
            
            print(f"\n⏳ جاري التوليد ({steps} خطوة، {num_images} صورة)...")
            
            # توليد الصور
            images = generator.generate(
                prompt=prompt,
                num_images=num_images,
                steps=steps
            )
            
            # حفظ الصور
            generator.save_images(images)
            
            print("\n✅ تم إنشاء الصور بنجاح!\n")
            
        except ValueError:
            print("❌ إدخال غير صحيح! الرجاء إدخال أرقام صحيحة.\n")
        except Exception as e:
            print(f"❌ حدث خطأ: {e}\n")


if __name__ == "__main__":
    interactive_mode()
