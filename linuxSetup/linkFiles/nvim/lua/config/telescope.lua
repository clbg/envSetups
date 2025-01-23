local M = {}

function M.setup()
  local actions = require "telescope.actions"
  local telescope = require "telescope"

  telescope.setup {
    defaults = {
      mappings = {
        i = {
          ["<C-j>"] = actions.move_selection_next,
          ["<C-k>"] = actions.move_selection_previous,
          ["<C-n>"] = actions.cycle_history_next,
          ["<C-p>"] = actions.cycle_history_prev,
        },
      },
    },

    extensions = {
      fzf = {
        fuzzy = true,                 -- false will only do exact matching
        override_generic_sorter = true, -- override the generic sorter
        override_file_sorter = true,  -- override the file sorter
        case_mode = "smart_case",     -- or "ignore_case" or "respect_case"
        -- the default case_mode is "smart_case"
      }
    }
  }

  telescope.load_extension "fzf"
  telescope.load_extension "project"   -- telescope-project.nvim
  telescope.load_extension "repo"
  telescope.load_extension "file_browser"
  telescope.load_extension "projects"   -- project.nvim
end

return M
