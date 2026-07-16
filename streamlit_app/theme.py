"""
Theme controls for
StockVision Forecast V2.
"""

import json

import streamlit as st
import streamlit.components.v1 as components


THEME_VARS = {
    "dark": {
        "--glass-bg": "rgba(15, 23, 42, 0.55)",
        "--glass-bg-strong": "rgba(15, 23, 42, 0.72)",
        "--glass-border": "rgba(255, 255, 255, 0.14)",
        "--glass-border-strong": "rgba(255, 255, 255, 0.24)",
        "--glass-shadow": "0 18px 50px rgba(2, 6, 23, 0.28)",
        "--text-primary": "#f8fbff",
        "--text-secondary": "rgba(248, 251, 255, 0.76)",
        "--accent": "#7dd3fc",
        "--accent-strong": "#5eead4",
        "--app-bg": "linear-gradient(135deg, #0a1020 0%, #0f172a 45%, #111827 100%)",
        "--app-glow-1": "rgba(56, 189, 248, 0.16)",
        "--app-glow-2": "rgba(45, 212, 191, 0.12)",
        "--title-shadow": "0 1px 12px rgba(56, 189, 248, 0.12)",
        "--metric-hover-bg": "rgba(15, 23, 42, 0.64)",
        "--metric-hover-border": "rgba(255, 255, 255, 0.28)",
        "--metric-hover-shadow": "0 22px 54px rgba(2, 6, 23, 0.34)",
        "--sidebar-bg": "linear-gradient(180deg, rgba(15, 23, 42, 0.78), rgba(15, 23, 42, 0.56))",
        "--header-bg": "rgba(15, 23, 42, 0.44)",
        "--header-border": "rgba(255, 255, 255, 0.08)",
        "--button-bg": "linear-gradient(135deg, rgba(56, 189, 248, 0.22), rgba(45, 212, 191, 0.16))",
        "--button-hover-bg": "linear-gradient(135deg, rgba(56, 189, 248, 0.3), rgba(45, 212, 191, 0.24))",
        "--button-hover-border": "rgba(255, 255, 255, 0.34)",
        "--button-hover-shadow": "0 24px 40px rgba(2, 6, 23, 0.22)",
        "--input-focus-border": "rgba(255, 255, 255, 0.26)",
        "--input-focus-shadow": "0 0 0 1px rgba(56, 189, 248, 0.22), 0 10px 24px rgba(2, 6, 23, 0.2)",
        "--details-bg": "rgba(15, 23, 42, 0.46)",
        "--tabs-bg": "rgba(15, 23, 42, 0.34)",
        "--tabs-active-bg": "rgba(255, 255, 255, 0.12)",
        "--scroll-track": "rgba(15, 23, 42, 0.22)",
        "--scroll-thumb": "linear-gradient(180deg, rgba(56, 189, 248, 0.55), rgba(45, 212, 191, 0.55))",
        "--scroll-thumb-border": "rgba(15, 23, 42, 0.16)",
        "--hr-border": "rgba(255, 255, 255, 0.08)",
    },
    "light": {
        "--glass-bg": "rgba(255, 255, 255, 0.44)",
        "--glass-bg-strong": "rgba(255, 255, 255, 0.62)",
        "--glass-border": "rgba(255, 255, 255, 0.62)",
        "--glass-border-strong": "rgba(255, 255, 255, 0.82)",
        "--glass-shadow": "0 18px 50px rgba(15, 23, 42, 0.12)",
        "--text-primary": "#0f172a",
        "--text-secondary": "rgba(15, 23, 42, 0.74)",
        "--accent": "#0284c7",
        "--accent-strong": "#0f766e",
        "--app-bg": "linear-gradient(135deg, #dff4ff 0%, #eef7ff 46%, #f8fffd 100%)",
        "--app-glow-1": "rgba(125, 211, 252, 0.42)",
        "--app-glow-2": "rgba(167, 243, 208, 0.34)",
        "--title-shadow": "0 2px 10px rgba(255, 255, 255, 0.42)",
        "--metric-hover-bg": "rgba(255, 255, 255, 0.52)",
        "--metric-hover-border": "rgba(255, 255, 255, 0.88)",
        "--metric-hover-shadow": "0 22px 54px rgba(15, 23, 42, 0.16)",
        "--sidebar-bg": "linear-gradient(180deg, rgba(255, 255, 255, 0.58), rgba(255, 255, 255, 0.3))",
        "--header-bg": "rgba(255, 255, 255, 0.46)",
        "--header-border": "rgba(255, 255, 255, 0.42)",
        "--button-bg": "linear-gradient(135deg, rgba(14, 165, 233, 0.18), rgba(20, 184, 166, 0.14))",
        "--button-hover-bg": "linear-gradient(135deg, rgba(14, 165, 233, 0.28), rgba(20, 184, 166, 0.22))",
        "--button-hover-border": "rgba(255, 255, 255, 0.95)",
        "--button-hover-shadow": "0 24px 40px rgba(15, 23, 42, 0.14)",
        "--input-focus-border": "rgba(255, 255, 255, 0.95)",
        "--input-focus-shadow": "0 0 0 1px rgba(14, 165, 233, 0.22), 0 10px 24px rgba(15, 23, 42, 0.12)",
        "--details-bg": "rgba(255, 255, 255, 0.34)",
        "--tabs-bg": "rgba(255, 255, 255, 0.34)",
        "--tabs-active-bg": "rgba(255, 255, 255, 0.62)",
        "--scroll-track": "rgba(255, 255, 255, 0.22)",
        "--scroll-thumb": "linear-gradient(180deg, rgba(14, 165, 233, 0.45), rgba(20, 184, 166, 0.45))",
        "--scroll-thumb-border": "rgba(255, 255, 255, 0.16)",
        "--hr-border": "rgba(15, 23, 42, 0.12)",
    },
}


THEME_KEYS = list(THEME_VARS["dark"].keys())


def _theme_script(mode):
    if mode == "system":
        actions = "\n".join(
            f"root.style.removeProperty({json.dumps(key)});"
            for key in THEME_KEYS
        )
    else:
        actions = "\n".join(
            f"root.style.setProperty({json.dumps(key)}, {json.dumps(value)});"
            for key, value in THEME_VARS[mode].items()
        )

    return f"""
<script>
(function() {{
    const root = window.parent.document.documentElement;
    {actions}
}})();
</script>
"""


def render_theme_controls():
    """Render a small System / Dark / Light theme switch for the current session."""

    if "theme_mode" not in st.session_state:
        st.session_state.theme_mode = "system"

    st.caption("Theme")

    col1, col2, col3 = st.columns(3)

    if col1.button("System", use_container_width=True):
        st.session_state.theme_mode = "system"

    if col2.button("Dark", use_container_width=True):
        st.session_state.theme_mode = "dark"

    if col3.button("Light", use_container_width=True):
        st.session_state.theme_mode = "light"

    mode = st.session_state.theme_mode

    components.html(_theme_script(mode), height=0)
