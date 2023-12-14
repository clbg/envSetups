local buf, win
local snake = { { x = 5, y = 5 } }
local direction = { x = 0, y = 0 }
local game_running = true

local function create_window()
  buf = vim.api.nvim_create_buf(false, true)
  local width = 50
  local height = 20
  local opts = {
    style = 'minimal',
    relative = 'editor',
    width = width,
    height = height,
    row = (vim.o.lines - height) / 2,
    col = (vim.o.columns - width) / 2
  }

  win = vim.api.nvim_open_win(buf, true, opts)
  vim.api.nvim_win_set_option(win, 'cursorline', true)
end

local function update_snake()
  local new_head = { x = snake[1].x + direction.x, y = snake[1].y + direction.y }
  table.insert(snake, 1, new_head)
  table.remove(snake)
end

local function draw()
  vim.api.nvim_buf_set_lines(buf, 0, -1, false, {})
  local lines = {}
  for y = 1, 20 do
    local line = ""
    for x = 1, 50 do
      local is_snake = false
      for _, segment in ipairs(snake) do
        if segment.x == x and segment.y == y then
          is_snake = true
          break
        end
      end
      if is_snake then
        line = line .. "#"
      else
        line = line .. " "
      end
    end
    table.insert(lines, line)
  end
  vim.api.nvim_buf_set_lines(buf, 0, -1, false, lines)
end

local function game_loop()
  if not game_running then
    vim.api.nvim_win_close(win, true)
    return
  end
  update_snake()
  draw()
  vim.defer_fn(game_loop, 200)
end

local function set_keymaps()
  local mappings = {
    a = function() direction = { x = -1, y = 0 } end,
    s = function() direction = { x = 0, y = 1 } end,
    d = function() direction = { x = 1, y = 0 } end,
    w = function() direction = { x = 0, y = -1 } end,
    q = function() game_running = false end
  }

  for k, v in pairs(mappings) do
    vim.api.nvim_set_keymap('n', k, '', { noremap = true, silent = true, callback = v })
  end
end

local function start_game()
  create_window()
  set_keymaps()
  game_loop()
end

local M = {}
M.start_game=start_game
return M

