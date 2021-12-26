from math import *

#target_game='Final fantasy'
target_game='DRAGON QUEST'
#target_game='Tales Of'
#target_game='龍が如く'
#target_game='グラブル'
#target_game='ぷよぷよ'
#target_game='テトリス'


# 閲覧したゲーム
user_view_games_list={
  1: [
    'Final fantasy', 'DRAGON QUEST', 'Tales Of'
  ],
  2: [
    'Final fantasy', 'DRAGON QUEST', '龍が如く'
  ],
  3: [
    'Final fantasy', 'グラブル'
  ],
  4: [
    'DRAGON QUEST', 'グラブル'
  ],
  5: [
    'ぷよぷよ', 'テトリス'
  ]
}


def get_recommend(title):

  all_games = []
  score_list = {} # ゲームごとの関連度を保存する
  target_user_view_keys = set()

  # 全てのゲームを取得する
  for user_view_games in user_view_games_list.values():
    all_games.extend(user_view_games)

  all_games=set(all_games)

  # 確認対象の集合を作成する
  for k, user_view_games in user_view_games_list.items():
    if ( title in user_view_games ):
      target_user_view_keys.add(k)

  # 確認対象の集合を確認しながら Jaccard係数 を算出する
  for game in all_games:
    if (game == title):
      continue
    tmp_keys = set()
    for k, user_view_games in user_view_games_list.items():
      if ( game in user_view_games ):
        tmp_keys.add(k)
    tmp_intersection = tmp_keys.intersection(target_user_view_keys)
    score_list[game] = len(tmp_intersection) / (len(tmp_keys) + len(target_user_view_keys) - len(tmp_intersection))

  print(score_list)


print('探索対象「%s」' % target_game)
get_recommend(target_game)
