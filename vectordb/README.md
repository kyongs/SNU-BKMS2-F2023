# VectorDB (pgvector)

This practice will teach you
- How to create embeddings from content using the OpenAI API
- How to use PostgreSQL as a vector database and store embeddings data in it using pgvector.
- How to use embeddings retrieved from a vector database to augment LLM generation.

> We use a PostgreSQL database with pgvector installed which is hosted on Supabase.(Based on Google Colab) You can create your own cloud PostgreSQL database in minutes [at this link](https://supabase.com/dashboard/projects) to follow along. You can also use a local PostgreSQL database if you prefer.


## Configurations
```
from google.colab import drive
```
- blog_posts_data.csv
- practice.ipynb