import plotly.graph_objects as go
import pandas as pd

from scrapers.config import SessionLocal
from stats.models import Album


def genre_chart_view(request):

    session = SessionLocal()

    try:
        albums = session.query(Album.genre).all()
        df = pd.DataFrame(albums, columns=['genre'])
    finally:
        session.close()

    genre_count = df['genre'].value_counts().reset_index()
    genre_count.columns = ['genre', 'count']

    top_5_genres = genre_count.head(5)

    fig = go.Figure(data=[
        go.Bar(
            x=top_5_genres['genre'],
            y=top_5_genres['count'],
            marker=dict(color='rgba(154, 197, 150, 0.6)'),
            textposition='auto'
        )
    ])

    fig.update_layout(
        xaxis=dict(
            showgrid=False,
            showticklabels=False
        ),
        yaxis=dict(
            showgrid=False,
            showticklabels=False
        ),
        width=500,
        height=350,
        margin=dict(l=0, r=0, t=0, b=0),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
    )

    chart = fig.to_html(full_html=False,
                        config={"displayModeBar": False, "responsive": True})

    return chart
