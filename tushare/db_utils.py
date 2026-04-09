import duckdb

def init_db():
    """初始化数据库连接
    """
    path = "../python/mydb.duckdb";
    try:
        return duckdb.connect(path, read_only=False)
    except duckdb.IOException as e:
        wrong_message = str(e)
        if any(keyword in wrong_message for keyword in ('Could not set lock', 'already open', '另一个程序', 'resource temporarily unavailable')):
            raise RuntimeError(
                f"数据库文件 '{path}' 正被其他程序占用，请先关闭后重试。\n({wrong_message.splitlines()[0]})"
            ) from None
        raise

def select(query):
    """
    执行SQL查询并返回DataFrame

    Args:
        query: SQL查询语句
        
    Returns:
        DataFrame
    """
    conn = init_db()
    try:
        result = conn.execute(query).fetch_df()
        return result
    finally:
        conn.close()