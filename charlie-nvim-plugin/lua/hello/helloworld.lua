local M = {}

function M.sayHelloWorld()
  print('Hello world again!!')
  local buf = vim.api.nvim_create_buf(false, true)

  -- 为新缓冲区设置一些初始内容（可选）
  local lines = { "This is a new buffer", "with some initial text." }
  vim.api.nvim_buf_set_lines(buf, 0, -1, false, lines)

  -- 创建一个新窗口并在其中打开这个缓冲区
  local win = vim.api.nvim_open_win(buf, true, {
    relative = 'editor',
    width = 80,
    height = 20,
    col = 10,
    row = 10,
    style = 'minimal'
  })
end

return M
