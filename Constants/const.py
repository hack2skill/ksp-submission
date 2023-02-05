import __root__
bucket_name = 'xfactor-app'

image_file_extention = [".jpg", ".jpeg", ".tif", ".tiff", ".gif", ".png", ".psd", ".bmp", ".jfif"]
preference_images_dir = './Data/preference_images_dir'
profile_images_dir = './Data/profile_images_dir'

compare_from_profile_dp_image = "./Data/compare_profile_images/compare_from_profile_dp_image"
compare_to_test_image = "./Data/compare_profile_images/compare_to_test_image"

suspects_images_repo = "./Data/experiment_images_dir/images_main_repo"
# suspect_test_image = "./Data/experiment_images_dir/test_images_repo"
suspect_test_image = "static/img"

##----------------------  afghaniiit@gmail.com's MongoDB------------------------------------

# table1_profileVectorizedImages = "flask_test_table1_v1"
# table2_preferencesBasedMatchedProfiles = "flask_test_table2_v1"

##----------------------  Nitin's ex-factor-test MongoDB------------------------------------
table1_profileVectorizedImages = "ai_table1_profileVectorizedImages"
table2_preferencesBasedMatchedProfiles = "ai_table2_preferencesBasedMatchedProfiles"


aws_s3Bucket_url = "https://xfactor-app.s3.ap-south-1.amazonaws.com"

# aws_s3Bucket_url = "https://exfactor-prod.s3.ap-south-1.amazonaws.com/"

img_now = "img_now.jpg"
img_normal = "img_normal.jpg"
img_removed = "img_removed.jpg"
img_predict = "img_predicted.jpg"


##----------------------  For interests/hobbies ------------------------------------

interests_dict = {
            "creativity": [
                "art",
                "crafts",
                "dancing",
                "design",
                "make-up",
                "making videos",
                "photography",
                "singing",
                "writing"
            ],
            "film & tv": [
                "action and adventure",
                "animated",
                "anime",
                "bollywood",
                "comedy",
                "cooking shows",
                "crime",
                "documentaries",
                "drama",
                "fantasy",
                "game shows",
                "horror",
                "indie",
                "mystery",
                "reality shows",
                "rom-com",
                "romance",
                "sci-fi",
                "superhero",
                "thriller"
            ],
            "food & drink": [
                "beer",
                "biryani",
                "coffee",
                "foodie",
                "gin",
                "maggi",
                "pizza",
                "sweet tooth",
                "vegan",
                "vegatarian",
                "whisly",
                "wine"
            ],
            "going out": [
                "bars",
                "festivals",
                "gigs",
                "museaums and galleries",
                "nightclubs",
                "stand up",
                "theatre"
            ],
            "music": [
                "afro",
                "arab",
                "blues",
                "classical",
                "country",
                "desi",
                "edm",
                "eletronic",
                "folk & acoustic",
                "funk",
                "hip hop",
                "house",
                "indie",
                "jazz",
                "k-pop",
                "latin",
                "metal",
                "pop",
                "punjabi",
                "punk",
                "r&b",
                "rap",
                "reggae",
                "rock",
                "soul",
                "sufi",
                "techno"
            ],
            "pets": [
                "birds",
                "cats",
                "dogs",
                "fish",
                "lizards",
                "rabbits",
                "snakes"
            ],
            "popular": [
                "beaches",
                "coffee",
                "cooking",
                "dogs",
                "hiking trips",
                "video games"
            ],
            "reading": [
                "action and adventure",
                "biographies",
                "classics",
                "comedy",
                "comic books",
                "crime",
                "fantasy",
                "history",
                "horror",
                "manga",
                "mystery",
                "philosophy",
                "poetry",
                "psychology",
                "romance",
                "sci-fi",
                "science",
                "thriller"
            ],
            "sports": [
                "americal football",
                "athletics",
                "badminton",
                "baseball",
                "boxing",
                "cricket",
                "cycling",
                "football",
                "golf",
                "gym",
                "gymnastics",
                "martial arts",
                "meditation",
                "running",
                "skiing",
                "surfing",
                "swimming",
                "table tennis",
                "volleyball",
                "yoga"
            ],
            "staying in": [
                "baking",
                "board games",
                "cooking",
                "gardening",
                "takeaways",
                "video games"
            ],
            "travelling": [
                "backpacking",
                "beaches",
                "camping",
                "city breaks",
                "country escapes",
                "fishing trips",
                "hiking trips",
                "road trips",
                "spa weekends",
                "winter sports"
            ],
            "values & traits": [
                "ambition",
                "being active",
                "being family-oriented",
                "being open-minded",
                "being romantic",
                "confidence",
                "creativity",
                "empathy",
                "intelligence",
                "positivity",
                "self-awareness",
                "sense of adventure",
                "sense of humour",
                "social awareness"
            ]
        }


# users_df_columns = ['user_id', 'name', 'sex_orientation', 'gender', 'dob','location']
# media_df_columns = ['media_id', 'user_id', 'type', 'media_url', 'dp']
#
# to_match_preference_image_folder = "./Assets/Data/Images/TestCases"
# match_with_profile_images_folder = "./Assets/Data/Images/RefProfileImages"
#
# pickled_database_path = "./Assets/Data/Images/RefProfileImages/PickledFile_reference_images_database.pickle"


WEIGHTS = [
  'conv1', 'bn1', 'conv2', 'bn2', 'conv3', 'bn3',
  'inception_3a_1x1_conv', 'inception_3a_1x1_bn',
  'inception_3a_pool_conv', 'inception_3a_pool_bn',
  'inception_3a_5x5_conv1', 'inception_3a_5x5_conv2', 'inception_3a_5x5_bn1', 'inception_3a_5x5_bn2',
  'inception_3a_3x3_conv1', 'inception_3a_3x3_conv2', 'inception_3a_3x3_bn1', 'inception_3a_3x3_bn2',
  'inception_3b_3x3_conv1', 'inception_3b_3x3_conv2', 'inception_3b_3x3_bn1', 'inception_3b_3x3_bn2',
  'inception_3b_5x5_conv1', 'inception_3b_5x5_conv2', 'inception_3b_5x5_bn1', 'inception_3b_5x5_bn2',
  'inception_3b_pool_conv', 'inception_3b_pool_bn',
  'inception_3b_1x1_conv', 'inception_3b_1x1_bn',
  'inception_3c_3x3_conv1', 'inception_3c_3x3_conv2', 'inception_3c_3x3_bn1', 'inception_3c_3x3_bn2',
  'inception_3c_5x5_conv1', 'inception_3c_5x5_conv2', 'inception_3c_5x5_bn1', 'inception_3c_5x5_bn2',
  'inception_4a_3x3_conv1', 'inception_4a_3x3_conv2', 'inception_4a_3x3_bn1', 'inception_4a_3x3_bn2',
  'inception_4a_5x5_conv1', 'inception_4a_5x5_conv2', 'inception_4a_5x5_bn1', 'inception_4a_5x5_bn2',
  'inception_4a_pool_conv', 'inception_4a_pool_bn',
  'inception_4a_1x1_conv', 'inception_4a_1x1_bn',
  'inception_4e_3x3_conv1', 'inception_4e_3x3_conv2', 'inception_4e_3x3_bn1', 'inception_4e_3x3_bn2',
  'inception_4e_5x5_conv1', 'inception_4e_5x5_conv2', 'inception_4e_5x5_bn1', 'inception_4e_5x5_bn2',
  'inception_5a_3x3_conv1', 'inception_5a_3x3_conv2', 'inception_5a_3x3_bn1', 'inception_5a_3x3_bn2',
  'inception_5a_pool_conv', 'inception_5a_pool_bn',
  'inception_5a_1x1_conv', 'inception_5a_1x1_bn',
  'inception_5b_3x3_conv1', 'inception_5b_3x3_conv2', 'inception_5b_3x3_bn1', 'inception_5b_3x3_bn2',
  'inception_5b_pool_conv', 'inception_5b_pool_bn',
  'inception_5b_1x1_conv', 'inception_5b_1x1_bn',
  'dense_layer'
]

conv_shape = {
  'conv1': [64, 3, 7, 7],
  'conv2': [64, 64, 1, 1],
  'conv3': [192, 64, 3, 3],
  'inception_3a_1x1_conv': [64, 192, 1, 1],
  'inception_3a_pool_conv': [32, 192, 1, 1],
  'inception_3a_5x5_conv1': [16, 192, 1, 1],
  'inception_3a_5x5_conv2': [32, 16, 5, 5],
  'inception_3a_3x3_conv1': [96, 192, 1, 1],
  'inception_3a_3x3_conv2': [128, 96, 3, 3],
  'inception_3b_3x3_conv1': [96, 256, 1, 1],
  'inception_3b_3x3_conv2': [128, 96, 3, 3],
  'inception_3b_5x5_conv1': [32, 256, 1, 1],
  'inception_3b_5x5_conv2': [64, 32, 5, 5],
  'inception_3b_pool_conv': [64, 256, 1, 1],
  'inception_3b_1x1_conv': [64, 256, 1, 1],
  'inception_3c_3x3_conv1': [128, 320, 1, 1],
  'inception_3c_3x3_conv2': [256, 128, 3, 3],
  'inception_3c_5x5_conv1': [32, 320, 1, 1],
  'inception_3c_5x5_conv2': [64, 32, 5, 5],
  'inception_4a_3x3_conv1': [96, 640, 1, 1],
  'inception_4a_3x3_conv2': [192, 96, 3, 3],
  'inception_4a_5x5_conv1': [32, 640, 1, 1,],
  'inception_4a_5x5_conv2': [64, 32, 5, 5],
  'inception_4a_pool_conv': [128, 640, 1, 1],
  'inception_4a_1x1_conv': [256, 640, 1, 1],
  'inception_4e_3x3_conv1': [160, 640, 1, 1],
  'inception_4e_3x3_conv2': [256, 160, 3, 3],
  'inception_4e_5x5_conv1': [64, 640, 1, 1],
  'inception_4e_5x5_conv2': [128, 64, 5, 5],
  'inception_5a_3x3_conv1': [96, 1024, 1, 1],
  'inception_5a_3x3_conv2': [384, 96, 3, 3],
  'inception_5a_pool_conv': [96, 1024, 1, 1],
  'inception_5a_1x1_conv': [256, 1024, 1, 1],
  'inception_5b_3x3_conv1': [96, 736, 1, 1],
  'inception_5b_3x3_conv2': [384, 96, 3, 3],
  'inception_5b_pool_conv': [96, 736, 1, 1],
  'inception_5b_1x1_conv': [256, 736, 1, 1],
}