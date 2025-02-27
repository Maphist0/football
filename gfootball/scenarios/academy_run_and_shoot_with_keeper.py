from . import *

def build_scenario(builder):
  builder.SetFlag('game_duration', 400)
  builder.SetFlag('deterministic', False)
  builder.SetFlag('offsides', False)
  builder.SetFlag('end_episode_on_score', True)
  builder.SetFlag('end_episode_on_out_of_play', True)
  builder.SetFlag('end_episode_on_possession_change', True)
  builder.SetBallPosition(0.5, 0)

  builder.SetTeam(Team.e_Left)
  builder.AddPlayer(-1.0, 0.0, e_PlayerRole_GK)
  builder.AddPlayer(0.45, 0, e_PlayerRole_CF)

  builder.SetTeam(Team.e_Right)
  builder.AddPlayer(-1.0, 0.0, e_PlayerRole_GK, True)