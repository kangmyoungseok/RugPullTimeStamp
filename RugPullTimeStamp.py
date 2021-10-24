#RugPull이 일어난 시점의 TimeStamp를 구해서 Paris_v1.x파일에 추가한다.
#Pre-Condition : Pairs_v1.4.csv파일
import json
import pandas as pd



# json 파일과 Pair를 메모리에 먼저 올린다.
with open('./swap_sample.json', 'r') as f:
    swap_data = json.load(f)

with open('./mint_sample.json', 'r') as f:
    mint_data = json.load(f)

with open('./burn_sample.json', 'r') as f:
    burn_data = json.load(f)

datas = pd.read_csv('/content/drive/MyDrive/Pairs_v1.4.csv',usecols=['id','token0.name','token1.name']).to_dict('records')
token_pairs = {}
for data in datas:
    tmp_dict = {data['id'] : {'token0.name':data['token0.name'],'token1.name':data['token1.name']}}
    token_pairs.update(tmp_dict)
del datas


# Pair_address를 주면 토큰이 token0인지 token1인지 판단. 0,1로 리턴
def token_index(pair_address): 
    if(token_pairs[pair_address]['token0.name'] =='Wrapped Ether' ):
      return  1
    else:
      return 0
  

for pair_address,swap_list in mint_data.items():
    mint_data_transaction = mint_data[pair_address]
    swap_data_transaction = swap_data[pair_address]
    burn_data_transaction = burn_data[pair_address]
    if(token_index(pair_address) == 1): #amount1이 토큰 amount0이 이더
      initial_Liquidity_Eth = mint_data_transaction[0]['amount0']
    else:
      initial_Liquidity_Eth = mint_data_transaction[0]['amount1']

    print(initial_Liquidity_Eth)
  

  