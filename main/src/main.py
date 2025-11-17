# Fast api lib
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# Other
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
        This function will run once when the FastAPI server starts.
    """
    print("🚀 Server is starting, running initialization script...")
    # Creates db tables if them do not exist yet

    # The app is running after this point
    yield

    # --- Shutdown logic (runs once when the server stops) ---
    print("🛑 Server is shutting down...")

# Initiate fast api server
app = FastAPI(lifespan=lifespan)

# CORS for Storybook/Local Dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register global exception handler
# app.add_exception_handler(CustomException, exception_handler)

# Include routing to access domain-specific controllers
# TODO app.include_router()