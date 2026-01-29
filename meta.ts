export const meta = {
  /**
   * Type 1: Generated Skills (from submodules)
   * Repository URLs to clone and generate skills from.
   */
  submodules: {},

  /**
   * Type 2: Synced Skills (from other repos)
   * Configuration for syncing specific skills from vendor repositories.
   */
  vendors: {},

  /**
   * Type 3: Hand-written Skills
   * Locally maintained skills that don't require generation or syncing.
   */
  skills: [
    {
      name: 'web',
      description: 'Preferred stack for web projects using Bun, Vite, React 19, and Tailwind 4',
    },
    {
      name: 'server',
      description: 'Preferred stack for backend services using uv, FastAPI, Python 3.12+, and AI tools',
    },
    {
      name: 'slides',
      description: 'Generates high-quality, single-file HTML interactive slide decks',
    },
  ],
}
