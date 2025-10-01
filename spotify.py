import pandas as pd
import plotly.express as px
import plotly.io as pio
from pathlib import Path

pio.renderers.default = "browser"

CSV_PATH = Path(r"C:\Users\agatha55289086\Desktop\Agatha\em aula\spotify_new.csv")
SAIDA_DIR = Path(r"C:\Users\agatha55289086\Desktop\Agatha\em aula\saida")
SAIDA_DIR.mkdir(parents=True, exist_ok=True)

def main():
    df = pd.read_csv(CSV_PATH)
    print("\n=== 5 primeiras linhas ===")
    print(df.head(5))

    colunas_numericas = df.select_dtypes(include=['number']).columns.tolist()
    df[colunas_numericas] = df.groupby('subscription_type')[colunas_numericas].transform(lambda g: g.fillna(g.mean()))
    print("\n=== Contagem de valores ausentes após preenchimento ===")
    print(df[colunas_numericas].isna().sum())

    df['gender'] = df['gender'].replace({'Male':'M', 'Female':'F'})
    df['country'] = df['country'].fillna('Desconhecido')
    df = df.rename(columns={'listening_time':'minutos_por_dia'})
    if 'ads_listened_per_week' in df.columns:
        df = df.drop(columns=['ads_listened_per_week'])

    before_count = len(df)
    df = df[df['age'] >= 13].copy()
    removed = before_count - len(df)
    print(f"\nRemovidos {removed} usuários com age < 13. Registros atuais: {len(df)}")

    print(f"\nIdade média dos usuários: {df['age'].mean():.2f} anos")
    print("\nTempo médio de escuta diário por assinatura:")
    print(df.groupby('subscription_type')['minutos_por_dia'].mean())

    print("\nTop 10 países por quantidade de usuários:")
    print(df['country'].value_counts().head(10))
    print("\nSkip rate médio por tipo de dispositivo:")
    print(df.groupby('device_type')['skip_rate'].mean())

    print(f"\nQuantidade total de músicas tocadas: {df['songs_played_per_day'].sum()}")
    print(f"\nUsuários Free com >180 minutos/dia: {len(df[(df['minutos_por_dia']>180) & (df['subscription_type'].str.lower()=='free')])}")

    media_musicas = df.groupby('subscription_type')['songs_played_per_day'].mean().reset_index()
    fig1 = px.bar(media_musicas, x='subscription_type', y='songs_played_per_day',
                  color='subscription_type', title='Média de músicas por dia por assinatura',
                  labels={'songs_played_per_day':'Média de músicas/dia','subscription_type':'Assinatura'})
    fig1.show()
    fig1.write_html(SAIDA_DIR / "grafico_media_musicas.html")

    fig2 = px.histogram(df, x='age', nbins=20, title='Distribuição de Idades', color_discrete_sequence=['orange'])
    fig2.show()
    fig2.write_html(SAIDA_DIR / "grafico_hist_idade.html")

    churn_counts = df['is_churned'].value_counts().reset_index()
    churn_counts.columns = ['Status','Quantidade']
    churn_counts['Status'] = churn_counts['Status'].map({0:'Ativo',1:'Cancelou'})
    fig3 = px.pie(churn_counts, values='Quantidade', names='Status', title='Proporção de cancelamentos',
                  color='Status', color_discrete_map={'Ativo':'green','Cancelou':'red'})
    fig3.show()
    fig3.write_html(SAIDA_DIR / "grafico_churn.html")

    fig4 = px.scatter(df, x='minutos_por_dia', y='skip_rate', color='subscription_type',
                      title='Minutos por dia vs Skip rate', labels={'minutos_por_dia':'Minutos/dia','skip_rate':'Skip rate'})
    fig4.show()
    fig4.write_html(SAIDA_DIR / "grafico_scatter.html")

    df_top5 = df.sort_values(by='minutos_por_dia', ascending=False).head(5)
    fig5 = px.bar(df_top5, x='user_id', y='minutos_por_dia', title='Top 5 usuários por minutos/dia',
                  labels={'user_id':'Usuário','minutos_por_dia':'Minutos/dia'}, color='minutos_por_dia')
    fig5.show()
    fig5.write_html(SAIDA_DIR / "grafico_top5_minutos.html")

    print(f"\nGráficos interativos salvos em: {SAIDA_DIR}")
    df.to_csv(SAIDA_DIR / 'spotify_processado.csv', index=False)
    print(f"Arquivo processado salvo em: {SAIDA_DIR / 'spotify_processado.csv'}")

if __name__ == '__main__':
    main()
