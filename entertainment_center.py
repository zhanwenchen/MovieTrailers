import fresh_tomatoes
import media


the_battle_of_algiers = media.Movie("The Battle of Algiers", "The last years of French colonial rule in Algeria",
                                "https://upload.wikimedia.org/wikipedia/en/a/aa/The_Battle_of_Algiers_poster.jpg",
                                "https://www.youtube.com/watch?v=Wd5Pz8KJeU4")

babel = media.Movie("Babel","A chain of events occure like the proverbial butterfly that flaps its wings",
                    "https://upload.wikimedia.org/wikipedia/en/a/a9/Babel_poster32.jpg",
                    "https://www.youtube.com/watch?v=gzrHrTVaqJs")

tokyo_story = media.Movie("Tokyo Story", "An old couple's visit to their children invokes a heartbreaking reality",
                          "https://upload.wikimedia.org/wikipedia/en/5/5f/Tokyo_Story_poster.jpg",
                          "https://www.youtube.com/watch?v=J_LXe4PIKtQ")

eat_drink_man_woman = media.Movie("Eat Drink Man Woman", "A man and his three daughters look for recipes for love",
                                  "https://upload.wikimedia.org/wikipedia/en/b/b4/Eat_Drink_Man_Woman.jpg",
                                  "https://www.youtube.com/watch?v=l7pKpO8NErU")

the_lives_of_others = media.Movie("The Lives of Others", "A surveillance agent gets involved in his subjects' lives",
                                  "https://upload.wikimedia.org/wikipedia/en/9/9f/Leben_der_anderen.jpg",
                                  "https://www.youtube.com/watch?v=n3_iLOp6IhM")

wadjda = media.Movie("Wadjda", "A girl competes in a Koran recitation competition in order to buy a bike",
                     "https://upload.wikimedia.org/wikipedia/en/f/f4/Wadjda_%28film%29.jpg",
                     "https://www.youtube.com/watch?v=3koigluYOH0")

a_separation = media.Movie("A Separation", "A family chosses between moving abroad for the child and a sick parent",
                           "https://upload.wikimedia.org/wikipedia/en/0/00/A_Separation.jpg",
                           "https://www.youtube.com/watch?v=58Onuy5USTc")

tinker_tailor_soldier_spy = media.Movie("Tinker Tailor Soldier Spy", "A spymaster must uncover a Soviet double agent",
                           "http://www.gstatic.com/tv/thumb/movieposters/8702008/p8702008_p_v8_ah.jpg",
                           "https://www.youtube.com/watch?v=LPKhWXhiMSw")

le_samourai = media.Movie("Le Samouraï", "A professional hitman gets driven into a corner after being caught in the act",
                                        "https://images-na.ssl-images-amazon.com/images/I/41VG2SMM32L.jpg",
                                        "https://www.youtube.com/watch?v=o0YcCb1bSNw")

omar = media.Movie("Omar", "Love is elusive for a Palestinian freedom fighter",
                   "http://t0.gstatic.com/images?q=tbn:ANd9GcSn5-dTCEB6nPu_q6x2shxSaqRHQ43lSr9_tEQvbVhpW_D-t1Uo",
                   "https://www.youtube.com/watch?v=OPcvn4Mtglc")

movies = [the_battle_of_algiers, babel, tokyo_story, eat_drink_man_woman, the_lives_of_others, wadjda, a_separation, tinker_tailor_soldier_spy, le_samourai, omar]
fresh_tomatoes.open_movies_page(movies)