import pandas as pd
from flask import render_template
from scraper import (
    scrape_quarterback_stats, scrape_runningback_stats, 
    scrape_wide_receiver_stats, scrape_tight_end_stats, 
    scrape_defense_stats, scrape_kicker_stats
)
from analyze import (
    calculate_qb_rating, calculate_rb_rating, 
    calculate_wr_rating, calculate_te_rating, 
    calculate_dst_rating, calculate_k_rating
)

def configure_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/qb')
    def show_qb_ratings():
        scrape_quarterback_stats()
        calculate_qb_rating()
        qb_rec_ratings = pd.read_csv('data/qb_rec_ratings.csv')
        return render_template('qb.html', qb_rec_ratings=qb_rec_ratings.to_dict(orient='records'))

    @app.route('/rb')
    def show_rb_ratings():
        scrape_runningback_stats()
        calculate_rb_rating()
        rb_rec_ratings = pd.read_csv('data/rb_rec_ratings.csv')
        return render_template('rb.html', rb_rec_ratings=rb_rec_ratings.to_dict(orient='records'))

    @app.route('/wr')
    def show_wr_ratings():
        scrape_wide_receiver_stats()
        calculate_wr_rating()
        wr_rec_ratings = pd.read_csv('data/wr_rec_ratings.csv')
        return render_template('wr.html', wr_rec_ratings=wr_rec_ratings.to_dict(orient='records'))

    @app.route('/te')
    def show_te_ratings():
        scrape_tight_end_stats()
        calculate_te_rating()
        te_rec_ratings = pd.read_csv('data/te_rec_ratings.csv')
        return render_template('te.html', te_rec_ratings=te_rec_ratings.to_dict(orient='records'))

    @app.route('/dst')
    def show_dst_ratings():
        scrape_defense_stats()
        calculate_dst_rating()
        dst_rec_ratings = pd.read_csv('data/dst_rec_ratings.csv')
        return render_template('dst.html', dst_rec_ratings=dst_rec_ratings.to_dict(orient='records'))

    @app.route('/kicker')
    def show_k_ratings():
        scrape_kicker_stats()
        calculate_k_rating()
        k_rec_ratings = pd.read_csv('data/k_rec_ratings.csv')
        return render_template('kicker.html', k_rec_ratings=k_rec_ratings.to_dict(orient='records'))