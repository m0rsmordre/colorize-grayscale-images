# colorize-grayscale-images
Grayscale Image
---------------------------------------------------------------------------------------------------------------------------
![example_grayscale](https://user-images.githubusercontent.com/42314954/118395004-bed1ee00-b650-11eb-88fd-a71c48470c47.jpg | width=500)


Colorized Image
---------------------------------------------------------------------------------------------------------------------------
![example_colorful](https://user-images.githubusercontent.com/42314954/118395014-cb564680-b650-11eb-917a-ef0583e33bd7.jpg | width=500)

## How to use
* First of all you need a DEEP AI API KEY
  sign up to website https://deepai.org/dashboard/profile and get your api key in profile section
* Edit the part of DEEP_AI_API_KEY = 'TOKEN' with your DEEP AI TOKEN
* Create bw and cf folders. Bw folder is for black and white images, cf folder is for colored images. Put some grayscale images in the bw folder
* Run script "python main.py"
* Script will scan files in bw folder and send a request to DEEP AI API image will be downloaded to cf folder as colorized

## Nasıl Kullanılır

* İlk önce bir adet api keyine ihtiyacınız olacak. Siteye kayıt olduktan sonra profile kısmından api keyinizi kopyalayın https://deepai.org/dashboard/profile
* DEEP_AI_API_KEY = "TOKEN" yazan kısımdaki TOKEN yazısını kendi api keyiniz ile değiştirin.
* bw ve cf isminde klasörleri oluşturmalısınız. bw isimli klasöre siyah beyaz fotoğraflarınızı atın
* Programı çalıştırın "python main.py"
* Program bw klasöründeki dosyaları tarayacak ve DEEP AI API'sine dosyaları gönderecek ve dosyaları teker teker cf klasörüne renklendirilmiş şekilde indirecektir.
