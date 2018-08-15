# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(zhenyuHuang)s
"""

import pandas as pd
import basicFun as bF
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties
from adjustText import adjust_text
import seaborn as sns

myfont = FontProperties(fname = 'C:\Windows\Fonts\simhei.ttf')

# clean data, together the pass and touch 
pass_df = pd.read_csv('PassTracking2017-18.csv')
touch_df = pd.read_csv('TouchTracking2017-18.csv')
touch_df = touch_df[['TOUCHES']]
pass_df = pass_df[['PLAYER_NAME','TEAM_ID','GP','MIN','PASSES_MADE','PASSES_RECEIVED','AST','FT_AST','SECONDARY_AST','POTENTIAL_AST','AST_ADJ','AST_TO_PASS_PCT','AST_TO_PASS_PCT_ADJ',]]
passAdvance_df = pd.concat([pass_df,touch_df],axis=1)
passAdvance_df = passAdvance_df[passAdvance_df['GP']>=10]
passAdvance_df = passAdvance_df[passAdvance_df['MIN']>=10]
passAdvance_df = bF.setName(passAdvance_df)
passAdvance_df['PassPct'] = passAdvance_df['PASSES_MADE']/passAdvance_df['TOUCHES']
team_df = pd.read_csv('team201718.csv')

passFinal = pd.DataFrame()
for i in team_df.index.tolist():
    teamid = team_df['TEAM_ID'][i]
    pass_df_tmp = passAdvance_df[passAdvance_df['TEAM_ID']==teamid]
    pass_df_tmp['FG_PCT'] = team_df['FG_PCT'][i]
    passFinal = pd.concat([passFinal,pass_df_tmp],axis=0)

passFinal['OffPCT'] = (passFinal['AST']/passFinal['POTENTIAL_AST'])-passFinal['FG_PCT']
#draw touches and assist

def drawTouchAST(shot_df):
    plt.figure(figsize=(8,8))
    plt.scatter(shot_df['TOUCHES'], shot_df['AST'],color='r',s=80,marker='o',
                alpha=0.4,linewidths=1)
    sns.regplot(shot_df['TOUCHES'], shot_df['AST'], scatter=False,line_kws={"color":"b","alpha":0.4,"lw":2})
    plt.grid(True, color = "0.75", linewidth = "0.75")  
    plt.xlabel(u'场均触球数',fontsize=16, fontproperties = myfont)
    plt.ylabel(u'场数助攻数',fontsize=16, fontproperties = myfont)
    plt.title(u'场均触球数VS助攻(made by jumpshot)',fontsize=12 ,
              x=0.25,y=1.01, fontweight=0,fontproperties = myfont)
    plt.xlim(40,100)
    plt.ylim(0,11)
    
    textlist = [444,256,324,217,39,423,139,326,235,462,195,149,278,307,41,313,86,464,396,433,430,313,515,73,
                111,452,212,485,392,398,112,117,41,173,345,108,64,300,74,294,175,118,251,28,323,47,372,299,126,81,328,100,317,308,97]
    textlist = list(set(textlist))
    texts=[]
    for i in textlist:
        name = shot_df['Name'][i]
        texts.append(plt.text(shot_df['TOUCHES'][i],shot_df['AST'][i],name,fontsize=8,fontweight='bold'))
    adjust_text(texts)
    return shot_df

def drawPassTendencyASTtoPoint(shot_df):
    shot_df = shot_df[shot_df['GP']>25]# select player GP > 25
    shot_df = shot_df[shot_df['MIN']>20]
    
    plt.figure(figsize=(12,8))
    plt.scatter(shot_df['PassPct'], shot_df['AST_TO_PASS_PCT_ADJ'],color='purple',s=100,marker='o',
                alpha=0.4,linewidths=1)
#    sns.regplot(shot_df['TOUCHES'], shot_df['AST'], scatter=False,line_kws={"color":"b","alpha":0.4,"lw":2})
    plt.grid(True, color = "0.75", linewidth = "0.75")  
    plt.xlabel(u'传球倾向',fontsize=18, fontproperties = myfont)
    plt.ylabel(u'传球助攻（修正）转化比',fontsize=18, fontproperties = myfont)
    plt.title(u'传球倾向VS得分转换(made by jumpshot)',fontsize=13 ,
              x=0.17,y=1.01, fontweight=0,fontproperties = myfont)
    plt.title(u"备注GP>25,Min>20，", loc='left', fontsize=13,
              style='italic',y=-0.08,fontproperties = myfont)
#    plt.xlim(40,100)
#    plt.ylim(0,11)
    
    textlist = [1]
    textlist = list(set(textlist))
    texts=[]
    for i in bF.get_index_RankFL('PassPct','AST_TO_PASS_PCT_ADJ',shot_df,15):
        name = shot_df['Name'][i]
        texts.append(plt.text(shot_df['PassPct'][i],shot_df['AST_TO_PASS_PCT_ADJ'][i],name,fontsize=8,fontweight='bold'))
    adjust_text(texts)
    return

def drawTMPCTAST(shot_df):
    shot_df = shot_df[shot_df['GP']>25]# select player GP > 25
    shot_df = shot_df[shot_df['MIN']>20]
  # enough amount assits pergame
    plt.figure(figsize=(12,8))
    plt.scatter(shot_df['AST_TO_PASS_PCT'], shot_df['OffPCT'],color='lime',s=200,marker='o',
                alpha=0.4,linewidths=1)
#    sns.regplot(shot_df['TOUCHES'], shot_df['AST'], scatter=False,line_kws={"color":"b","alpha":0.4,"lw":2})
    plt.grid(True, color = "0.75", linewidth = "0.75")  
    plt.xlabel(u'传球助攻转化比(AST/PASS)',fontsize=18, fontproperties = myfont)
    plt.ylabel(u'命中率提升',fontsize=18, fontproperties = myfont)
    plt.title(u'助攻转化与命中提升(made by jumpshot)',fontsize=13 ,
              x=0.17,y=1.01, fontweight=0,fontproperties = myfont)
    plt.title(u"备注GP>25,Min>20,AST>4", loc='left', fontsize=13,
              style='italic',y=-0.08,fontproperties = myfont)
#    plt.xlim(40,100)
#    plt.ylim(0,20)
    
    textlist = [1]
    textlist = list(set(textlist))
    texts=[]
    for i in bF.get_index_RankFL('AST_TO_PASS_PCT','OffPCT',shot_df,20):
        name = shot_df['Name'][i]
        texts.append(plt.text(shot_df['AST_TO_PASS_PCT'][i],shot_df['OffPCT'][i],name,fontsize=8,fontweight='bold'))
    adjust_text(texts)
    return shot_df

def typePlayer():
    
    shot_df = pd.read_csv('1718season_regular_data.csv')
    shot_df = shot_df[['PLAYER_NAME','GP','MIN','FGA','AST','TOV']]

    pass_df = passAdvance_df[['PASSES_MADE']]
    shot_df = pd.concat([shot_df,pass_df],axis=1)
    
    shot_df = shot_df[shot_df['GP']>25]# select player GP > 25
    shot_df = shot_df[shot_df['MIN']>20]
    shot_df = shot_df[shot_df['AST']>=4] # e
    shot_df['FGA/PASS'] = shot_df['FGA']/shot_df['PASSES_MADE']
    shot_df['AST/TOV'] = shot_df['AST']/shot_df['TOV']
    shot_df = bF.setName(shot_df)
    
    plt.figure(figsize=(12,8))
    plt.scatter(shot_df['FGA/PASS'], shot_df['AST/TOV'],color='b',s=200,marker='o',
                alpha=0.4,linewidths=1)

    plt.axhline(y=2,color='r',linewidth=1,linestyle='--')
    plt.axhline(y=3,color='r',linewidth=1,linestyle='--')
    plt.axhline(y=4,color='r',linewidth=1,linestyle='--')
    plt.grid(True, color = "0.75", linewidth = "0.75")  
    plt.xlabel(u'投篮传球比（FGA/PASS）',fontsize=18, fontproperties = myfont)
    plt.ylabel(u'助攻失误比(AST/TOV)',fontsize=18, fontproperties = myfont)
    plt.title(u'球员风格(made by jumpshot)',fontsize=13 ,
              x=0.12,y=1.01, fontweight=0,fontproperties = myfont)
    plt.title(u"备注GP>25,Min>20,AST>4", loc='left', fontsize=13,
              style='italic',y=-0.08,fontproperties = myfont)
#    plt.xlim(40,100)
#    plt.ylim(0,11)
    
    
    texts=[]
    for i in bF.get_index_RankFL('FGA/PASS','AST/TOV',shot_df,20):
        name = shot_df['Name'][i]
        texts.append(plt.text(shot_df['FGA/PASS'][i],shot_df['AST/TOV'][i],name,fontsize=8,fontweight='bold'))
    adjust_text(texts)
    return shot_df


x = drawTMPCTAST(passFinal)