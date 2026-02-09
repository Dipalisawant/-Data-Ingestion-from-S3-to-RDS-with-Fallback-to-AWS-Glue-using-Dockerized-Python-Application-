import mysql.connector
import boto3

try:
    conn = mysql.connector.connect(
        host="basic-db.cfka4iu0qhwz.ap-south-1.rds.amazonaws.com",
        user="admin",
        password="Dipu1234",
        database="testdb"
    )

    cursor = conn.cursor()
    cursor.execute("INSERT INTO users VALUES (1,'dipali','dipali@gmail.com')")
    conn.commit()

    print("✅ Data successfully inserted into RDS")

except Exception as e:
    print("❌ RDS insertion failed. Triggering Glue fallback")
    print(e)

    glue = boto3.client("glue", region_name="ap-south-1")
    glue.start_job_run(JobName="s3-to-rds-fallback-job")



