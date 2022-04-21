from dash.dependencies import Output, Input
import plotly.express as px
from run import app
from dataPreperation import get_dataFrame

df = get_dataFrame()
# tabs graphs update call back
@app.callback(Output('duration_fig1','figure'), [Input("tabs", "active_tab")])
def switch_tab(at):
    flag = False
    if at == "tab1_id":
        flag = False
    elif at == "tab2_id":
        flag = True
    duration = df[['title','duration']].sort_values('duration', ascending = flag)
    fig = px.bar(duration.iloc[:10,:10], x='title', y='duration',color='duration',
                 color_continuous_scale='RdGy',labels={'title':'Title of talk'})
    return fig