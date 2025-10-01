import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df = pd.read_csv(r"C:\Users\agatha55289086\Downloads\products-1000.csv")

size_map = {'S':'Small', 'M':'Medium', 'L':'Large'}
df['Size'] = df['Size'].replace(size_map)
df.dropna(inplace=True)
df.drop(columns=['Internal ID','Index'], inplace=True)
df = df[~df['Size'].isin(['5x7 in','12x18 in'])]

fig_scatter = px.scatter(df,
                         x='Price', 
                         y='Stock',
                         color='Category',
                         hover_data=['Size','Availability','Brand','Color'],
                         title="Distribuição de Preço x Estoque",
                         template='plotly_dark')

fig_hist = px.histogram(df,
                        x='Price',
                        color='Category',
                        barmode='overlay',
                        nbins=40,
                        title='Distribuição de Preços por Categoria',
                        template='plotly_white')

fig_box = px.box(df,
                 x='Size',
                 y='Price',
                 color='Size',
                 title='Distribuição de Preço por Tamanho',
                 template='plotly_dark')

num_cols = ['Price','Stock']
corr = df[num_cols].corr()
fig_heat = go.Figure(data=go.Heatmap(
    z=corr.values,
    x=corr.columns,
    y=corr.columns,
    colorscale='Viridis',
    zmin=-1,
    zmax=1
))
fig_heat.update_layout(title='Mapa de Correlação', template='plotly_white')

fig_dashboard = make_subplots(
    rows=2, cols=2,
    subplot_titles=('Preço x Estoque', 'Distribuição de Preços', 'Preço por Tamanho', 'Correlação'),
    specs=[[{"type": "scatter"}, {"type": "xy"}],
           [{"type": "box"}, {"type": "heatmap"}]]
)

for trace in fig_scatter.data:
    fig_dashboard.add_trace(trace, row=1, col=1)
for trace in fig_hist.data:
    fig_dashboard.add_trace(trace, row=1, col=2)
for trace in fig_box.data:
    fig_dashboard.add_trace(trace, row=2, col=1)
for trace in fig_heat.data:
    fig_dashboard.add_trace(trace, row=2, col=2)

fig_dashboard.update_layout(height=900, width=1200, title_text="Dashboard Interativo de Produtos")
fig_dashboard.show()

df.to_csv(r"C:\Users\agatha55289086\Downloads\produtos_processados.csv", index=False)
print("Arquivo produtos_processados.csv salvo com sucesso!")
