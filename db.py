import psycopg2




def get_posts():
    try:
        conn = psycopg2.connect(dbname="blog", user="postgres", password="123", host='localhost', port=5432)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM posts')
        
        posts = cursor.fetchall()
        
        cursor.close()
        conn.close()
        
        return [{'id': post[0], 'title': post[1], 'content': post[2]} for post in posts]
    except Exception as e:
        print('DB ERROR')



def get_post(pk):
    try:
        conn = psycopg2.connect(dbname="blog", user="postgres", password="123", host='localhost', port=5432)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM posts WHERE id=%d' % pk)
        
        post_qs = cursor.fetchone()
        
        cursor.close()
        conn.close()
        
        return {
            'id': post_qs[0],
            'title': post_qs[1],
            'content': post_qs[2]
        }
        
    except Exception as e:
        print('DB ERROR')