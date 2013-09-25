# -*- coding:utf-8 -*-

import app.models.db as db
import app.models.pager as pager

class Manga:

    # ==========================================
    # 
    # マンガ一覧を取得するやーつ
    # 
    # ==========================================

    def load(self, page):

        define_page = 10
        start = (page - 1) * define_page

        result = {}

        sql = "select count(id) as all_count from manga"
        db.con.execute(sql)
        result = db.con.fetchone()

        result["pagination"] = pager.Pagination(page, define_page, result["all_count"])

        sql = "select * from manga order by kana"
        sql += ' limit %s, %s'
        db.con.execute(sql, (start, define_page))
        result["mangas"] = db.con.fetchall()

        return result


    # ==========================================
    # 
    # マンガ単品を取得するやーつ
    # 
    # ==========================================
    def edit(self, id):

        sql = "select * from manga where id = %s"
        db.con.execute(sql, (id))
        return db.con.fetchone()


    # ==========================================
    # 
    # idがあったらdelフラグありで削除、無しで更新、idがなかったら新規追加
    # 
    # ==========================================
    def done(self, params):

        if params["id"]:

            if params["del"]:
                sql = "delete from manga where id = %s"
                db.con.execute(sql, (params["id"]))
            else:
                sql = "update manga set "
                sql += " num=%s"
                sql += ",name=%s"
                sql += ",kana=%s"
                sql += ",regdate=CURRENT_TIMESTAMP"
                sql += " where id = %s"
                db.con.execute(sql, (
                                    params["num"],
                                    params["name"],
                                    params["kana"],
                                    params["id"]
                                    ))

        else:

            sql = "insert into manga (num, name, kana, regdate) values (%s, %s, %s, CURRENT_TIMESTAMP)"
            db.con.execute(sql, (
                                params["num"],
                                params["name"],
                                params["kana"],
                                ))

        db.dbhandle.commit()
        return

