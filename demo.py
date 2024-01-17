
import pandas as pd
import streamlit.components.v1 as components
import streamlit as st
import pygwalker as pyg
# Adjust the width of the Streamlit page
st.set_page_config(
    page_title="Use Pygwalker In Streamlit",
    layout="wide"
)

st.title("Use Pygwalker In Streamlit")


vis_spec = r"""{"config":[{"config":{"defaultAggregated":true,"geoms":["auto"],"coordSystem":"generic","limit":-1},"encodings":{"dimensions":[{"dragId":"gw_-8gC","fid":"month_year_day","name":"month_year_day","basename":"month_year_day","semanticType":"nominal","analyticType":"dimension"},{"dragId":"gw_5XpU","fid":"scammer","name":"scammer","basename":"scammer","semanticType":"nominal","analyticType":"dimension"},{"dragId":"gw_mea_key_fid","fid":"gw_mea_key_fid","name":"Measure names","analyticType":"dimension","semanticType":"nominal"}],"measures":[{"dragId":"gw_jKuQ","fid":"Unnamed: 0","name":"Unnamed: 0","basename":"Unnamed: 0","analyticType":"measure","semanticType":"quantitative","aggName":"sum"},{"dragId":"gw_6bZ0","fid":"total_value_to_binance_sum","name":"total_value_to_binance_sum","basename":"total_value_to_binance_sum","analyticType":"measure","semanticType":"quantitative","aggName":"sum"},{"dragId":"gw_count_fid","fid":"gw_count_fid","name":"Row count","analyticType":"measure","semanticType":"quantitative","aggName":"sum","computed":true,"expression":{"op":"one","params":[],"as":"gw_count_fid"}},{"dragId":"gw_mea_val_fid","fid":"gw_mea_val_fid","name":"Measure values","analyticType":"measure","semanticType":"quantitative","aggName":"sum"}],"rows":[{"dragId":"gw_jgVJ","fid":"scammer","name":"scammer","basename":"scammer","semanticType":"nominal","analyticType":"dimension"}],"columns":[{"dragId":"gw_bBvW","fid":"month_year_day","name":"month_year_day","basename":"month_year_day","semanticType":"nominal","analyticType":"dimension"}],"color":[{"dragId":"gw_gGes","fid":"total_value_to_binance_sum","name":"total_value_to_binance_sum","basename":"total_value_to_binance_sum","analyticType":"measure","semanticType":"quantitative","aggName":"sum"}],"opacity":[],"size":[{"dragId":"gw_rwiJ","fid":"total_value_to_binance_sum","name":"total_value_to_binance_sum","basename":"total_value_to_binance_sum","analyticType":"measure","semanticType":"quantitative","aggName":"sum"}],"shape":[],"radius":[],"theta":[],"longitude":[],"latitude":[],"geoId":[],"details":[{"dragId":"gw_ft-Z","fid":"scammer","name":"scammer","basename":"scammer","semanticType":"nominal","analyticType":"dimension"}],"filters":[],"text":[]},"layout":{"showActions":false,"showTableSummary":false,"stack":"stack","interactiveScale":false,"zeroScale":true,"size":{"mode":"auto","width":320,"height":200},"format":{},"geoKey":"name","resolve":{"x":false,"y":false,"color":false,"opacity":false,"shape":false,"size":false}},"visId":"gw_k58Z","name":"Chart 1"}],"chart_map":{},"workflow_list":[{"workflow":[{"type":"view","query":[{"op":"aggregate","groupBy":["month_year_day","scammer"],"measures":[{"field":"total_value_to_binance_sum","agg":"sum","asFieldKey":"total_value_to_binance_sum_sum"}]}]}]}],"timezoneOffsetSeconds":-10800,"version":"0.4.1"}"""

df_graph = pd.read_csv("ETH_TO_BINANCE_NOV.csv")
# Generate the HTML using Pygwalker
pyg_html = pyg.to_html(df_graph, spec=vis_spec)
 
# Embed the HTML into the Streamlit app
components.html(pyg_html, height=1000, scrolling=True)